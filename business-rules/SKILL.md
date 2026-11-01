---
name: dotnet-business-rules
description: Technical .NET guidance for implementing business rules with clean architecture/DDD patterns (domain model, validation, specifications/policies, EF Core persistence boundaries), plus test strategy and operational concerns (auditing, idempotency, time/money, versioning). Use when designing or implementing business logic in C#/.NET services.
---

# .NET Business Rules

## Core Mandate
You are a **technical .NET (C#) expert** focused on building correct, maintainable **business rules**.

**Non‑negotiables**
- **Business rules live in the Domain** (not in controllers, not in EF Core entities as persistence models, and not scattered across UI).
- **Make invalid states unrepresentable** where practical (value objects, invariants, encapsulation).
- **Deterministic and testable** rules: no hidden `DateTime.Now`, static globals, random I/O.
- Prefer **explicit rule failures** (domain errors) over silent “fix-ups”.

## When to Use This Skill
Use this skill when the user asks for:
- Implementing business rules in **ASP.NET Core** APIs, background services, or worker processes
- Designing **domain models** (aggregates, entities, value objects) and rule enforcement
- Replacing “if/else soup” with patterns (Specification, Policy, Strategy)
- Building validation that goes beyond simple DTO validation
- Testing business logic (unit tests, property-based tests, golden master)

## Rule Placement (Quick Decision Table)
- **DTO / API validation** (shape & basic constraints): required fields, format, min/max length → FluentValidation/DataAnnotations.
- **Domain invariants** (must always hold): state transitions, totals, eligibility, pricing rules → Domain layer.
- **Cross-aggregate / external checks**: credit checks, inventory, risk scoring → Application layer orchestration + domain policies.
- **Persistence constraints**: unique indexes, FK constraints → Database + application conflict handling.

## Reference Architecture (Clean Architecture)
**API** → **Application** → **Domain** ← **Infrastructure**
- Domain has **no dependency** on EF Core / ASP.NET.
- Infrastructure implements repositories, time providers, message bus, etc.

## Recommended Workflow
1. **Clarify the rule**
   - Inputs, outputs, exceptions.
   - Edge cases: time zones, currency rounding, partial updates, concurrency.
   - Write acceptance examples (Given/When/Then).
2. **Model the domain**
   - Identify aggregate roots and boundaries.
   - Create value objects for money, date ranges, percentages, quantities.
3. **Encode invariants**
   - Guard clauses inside constructors/factory methods/state transition methods.
   - Expose behavior methods, avoid public setters.
4. **Select a rule pattern**
   - Few rules: keep it simple with domain methods.
   - Many composable rules: Specification/Policy objects.
   - Changing/tenant rules: Strategy + configuration, versioned rules.
5. **Write unit tests first for rule edge cases**
   - No database; pure domain tests.
   - Add application tests for orchestration and integration tests for persistence boundaries.
6. **Operationalize**
   - Audit important decisions.
   - Ensure idempotency for commands and events.
   - Make rule decisions observable (logs/metrics).

---

# Patterns for Business Rules

## 1) Domain Errors (Typed Failures)
Prefer returning a typed error (or throwing a domain exception that is caught at the boundary).

```csharp
public sealed record DomainError(string Code, string Message);

public static class OrderErrors
{
    public static DomainError CannotShipWithoutItems =>
        new("order.cannot_ship_without_items", "Order must contain at least one item before shipping.");
}
```

If you use functional style, return `Result<T>`; otherwise throw a **domain exception**.

```csharp
public sealed class DomainException : Exception
{
    public DomainError Error { get; }
    public DomainException(DomainError error) : base(error.Message) => Error = error;
}
```

## 2) Value Objects (Money, Dates, Identifiers)
Avoid `decimal` + string currency pairs everywhere.

```csharp
public sealed record Money(decimal Amount, string Currency)
{
    public static Money Of(decimal amount, string currency)
    {
        if (string.IsNullOrWhiteSpace(currency))
            throw new DomainException(new("money.currency_required", "Currency is required."));

        if (amount < 0)
            throw new DomainException(new("money.negative", "Money amount cannot be negative."));

        return new Money(decimal.Round(amount, 2, MidpointRounding.ToEven), currency.Trim().ToUpperInvariant());
    }

    public Money Add(Money other)
    {
        if (Currency != other.Currency)
            throw new DomainException(new("money.currency_mismatch", "Currency mismatch."));

        return Of(Amount + other.Amount, Currency);
    }
}
```

## 3) Aggregate Methods (Encapsulate Invariants)

```csharp
public sealed class Order
{
    private readonly List<OrderLine> _lines = new();

    public Guid Id { get; }
    public IReadOnlyCollection<OrderLine> Lines => _lines;
    public OrderStatus Status { get; private set; } = OrderStatus.Draft;

    public Order(Guid id) => Id = id;

    public void AddLine(ProductId productId, int quantity, Money unitPrice)
    {
        if (Status != OrderStatus.Draft)
            throw new DomainException(new("order.not_editable", "Only draft orders can be edited."));

        if (quantity <= 0)
            throw new DomainException(new("order.quantity_invalid", "Quantity must be positive."));

        _lines.Add(new OrderLine(productId, quantity, unitPrice));
    }

    public void Ship(IClock clock)
    {
        if (_lines.Count == 0)
            throw new DomainException(OrderErrors.CannotShipWithoutItems);

        if (Status != OrderStatus.Paid)
            throw new DomainException(new("order.not_paid", "Order must be paid before shipping."));

        Status = OrderStatus.Shipped;
        // Domain event could be raised here
        // AddEvent(new OrderShipped(Id, clock.UtcNow));
    }
}

public enum OrderStatus { Draft, Paid, Shipped, Cancelled }
public sealed record ProductId(string Value);
public sealed record OrderLine(ProductId ProductId, int Quantity, Money UnitPrice);

public interface IClock { DateTimeOffset UtcNow { get; } }
```

## 4) Specification Pattern (Composability)
Use when many eligibility rules exist.

```csharp
public interface ISpecification<in T>
{
    bool IsSatisfiedBy(T candidate);
}

public sealed class CanPlaceOrderSpec : ISpecification<Customer>
{
    public bool IsSatisfiedBy(Customer c) => c.IsActive && !c.IsBlocked;
}

public sealed class AndSpec<T>(ISpecification<T> left, ISpecification<T> right) : ISpecification<T>
{
    public bool IsSatisfiedBy(T candidate) => left.IsSatisfiedBy(candidate) && right.IsSatisfiedBy(candidate);
}
```

## 5) Policy Pattern (Rules That Need Context)
Use when rule evaluation needs extra inputs (time, configuration, external flags).

```csharp
public interface IDiscountPolicy
{
    Money Apply(Customer customer, Money subtotal, DateTimeOffset now);
}

public sealed class WeekendDiscountPolicy : IDiscountPolicy
{
    private readonly decimal _rate;
    public WeekendDiscountPolicy(decimal rate) => _rate = rate;

    public Money Apply(Customer customer, Money subtotal, DateTimeOffset now)
    {
        var isWeekend = now.DayOfWeek is DayOfWeek.Saturday or DayOfWeek.Sunday;
        if (!isWeekend) return subtotal;

        var discounted = subtotal.Amount * (1 - _rate);
        return Money.Of(discounted, subtotal.Currency);
    }
}
```

---

# Testing Guidance

## Unit Tests (Domain)
- Test **invariants** and **state transitions**.
- Prefer data-driven tests for edge cases.
- Avoid EF Core in domain tests.

Example (xUnit):
```csharp
[Fact]
public void Ship_Throws_When_No_Lines()
{
    var order = new Order(Guid.NewGuid());
    order.GetType();

    var ex = Assert.Throws<DomainException>(() => order.Ship(new FakeClock(DateTimeOffset.UtcNow)));
    Assert.Equal("order.cannot_ship_without_items", ex.Error.Code);
}

file sealed class FakeClock(DateTimeOffset now) : IClock
{
    public DateTimeOffset UtcNow => now;
}
```

## Integration Tests (Application/Infra)
- Validate rule persistence boundaries (unique constraints, concurrency tokens).
- Test mapping of `DomainException` → HTTP 400/409 with stable error codes.

---

# Operational Concerns (Common Rule Bugs)
- **Time**: store in UTC; convert at boundaries; inject `IClock`.
- **Money**: rounding mode; currency mismatches; avoid floating point.
- **Idempotency**: commands/events can be retried; store command IDs.
- **Concurrency**: use optimistic concurrency (`rowversion`) and handle conflicts.
- **Auditability**: record who/when/why a decision was made.

---

# Output Expectations
When you implement business rules, produce:
- A clear domain model (aggregates/value objects)
- Typed domain errors (stable error codes)
- Unit tests for rule edge cases
- Boundary mapping (HTTP/queue) that translates domain failures appropriately
