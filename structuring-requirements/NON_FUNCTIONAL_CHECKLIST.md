# Non-Functional Requirements (NFR) Checklist

Functional requirements describe *what* the system does. Non-Functional requirements describe *how well* it does it. Ensure every Epic/Feature has associated NFRs.

## Categories to Check

1.  **Performance:**
    *   Response time (e.g., API must return in < 200ms).
    *   Throughput (e.g., must handle 10,000 requests per second).
2.  **Scalability:**
    *   Expected data growth over 1 year / 5 years.
    *   Concurrent user limits.
3.  **Security & Compliance:**
    *   Authentication and Authorization (e.g., RBAC, SSO).
    *   Data encryption (at rest and in transit).
    *   Regulatory compliance (e.g., GDPR, HIPAA, PCI-DSS).
4.  **Reliability & Availability:**
    *   Uptime SLAs (e.g., 99.99% availability).
    *   Disaster recovery and backup strategies (RTO/RPO).
5.  **Usability:**
    *   Accessibility standards (e.g., WCAG 2.1 AA).
    *   Localization/Internationalization needs.