/* DotCare visit/service/package study - read-only trace.
   Select the target database in SSMS first. No data is changed.
   Samples: OPD 1424213, IPD 1415380, ER 1402590, AMB 1422482.
   Comparisons: AMB direct 1424316, virtual ER 1424347.
   IDs are local to AHJ Prelive; resolve them again in other environments.
*/
SET NOCOUNT ON;
SET LOCK_TIMEOUT 2000;
SET DEADLOCK_PRIORITY LOW;
DECLARE @VisitID bigint=1424213, @EntityID bigint=102;
SELECT DB_NAME() DatabaseName,@VisitID RequestedVisitID,@EntityID EntityID;
SELECT ID,VisitClassificationID,VisitTypeID,VisitStatusID,FinancialStatusID,AmountDue,AmountPaid,BalanceAmount,Wallet,CurrencyID,SpecialtyID,MainSpecialityID,CreatedDate,ArrivalDateTime,DischargeDate,InvoiceId,SyncStateID FROM VisitMgt.Visit WHERE ID=@VisitID AND EntityID=@EntityID;

-- Financial service, package-header and purchased-snapshot identities.
SELECT TOP(1500) s.ID VisitServiceID,s.VisitID,s.ServiceID ProductID,s.VisitServiceClassificationID,s.ProductCode,s.ServiceEnName,s.Quantity,s.UnitID,s.Price,s.PatientShare,s.CompanyShare,s.ServiceTaxDue,s.AllocatedAmount,s.DueAmount,s.OrderlineID,s.OrderID,s.ParentOrderLineID,s.BillingTransactionId,s.PatientPackageID,s.ServicePackageID,s.InPackageQuantity,s.PackageShare,s.PackageDiscount,s.IsDeleted,s.IsValidBillingState,s.BillingInvalidReason,h.VisitID PackagePurchasingVisitID,h.BillingTransactionId PackagePurchaseTransactionID,p.PackageID PackageDefinitionID FROM VisitMgt.VisitService s LEFT JOIN VisitMgt.VisitService h ON h.ID=s.ServicePackageID LEFT JOIN Billing.PatientPackage p ON p.ID=s.PatientPackageID WHERE s.VisitID=@VisitID AND s.EntityID=@EntityID ORDER BY s.ID OPTION(MAXDOP 1);

-- All assigned packages, including cancelled assignment history.
SELECT a.ID AssignmentID,a.VisitID AssignedVisitID,a.PackageServiceID,h.VisitID PurchasingVisitID,h.BillingTransactionId PurchasedSnapshotID,h.ServiceID PackageProductID,a.PurchasingDate,a.ExpiryDate,a.IsDeleted AssignmentDeleted,h.IsDeleted HeaderDeleted FROM VisitMgt.VisitPackagesAssignment a LEFT JOIN VisitMgt.VisitService h ON h.ID=a.PackageServiceID WHERE a.VisitID=@VisitID AND a.EntityID=@EntityID ORDER BY a.ID OPTION(MAXDOP 1);

-- Purchased terms are authoritative historical snapshots, not today's master rules.
SELECT p.ID PurchasedSnapshotID,p.PackageID,p.ProductID,p.Code,p.EnName,p.IsConsumeInOneVisit,p.IsTimeLimit,p.IsStartFromPurchasingDate,p.StartDate,p.ExpiryDate,p.IsConsumed,p.IsOffer,p.IsDeleted FROM Billing.PatientPackage p WHERE p.ID IN(SELECT BillingTransactionId FROM VisitMgt.VisitService WHERE VisitID=@VisitID AND EntityID=@EntityID AND VisitServiceClassificationID=8 UNION SELECT PatientPackageID FROM VisitMgt.VisitService WHERE VisitID=@VisitID AND EntityID=@EntityID AND PatientPackageID IS NOT NULL) OPTION(MAXDOP 1);
SELECT TOP(1000) d.ID,d.PatientPackageID,d.ProductID,d.BillingGroupID,d.UOMID,d.QuantityLimit,d.AmountLimit,d.DiscountPercentage,d.SpecificPrice,d.HasTerm,d.IsDeleted FROM Billing.PatientPackageDetail d WHERE d.PatientPackageID IN(SELECT BillingTransactionId FROM VisitMgt.VisitService WHERE VisitID=@VisitID AND EntityID=@EntityID AND VisitServiceClassificationID=8 UNION SELECT PatientPackageID FROM VisitMgt.VisitService WHERE VisitID=@VisitID AND EntityID=@EntityID AND PatientPackageID IS NOT NULL) ORDER BY d.PatientPackageID,d.ID OPTION(MAXDOP 1);

-- Indexed ServicePackageID follows consumption into other visits too.
SELECT TOP(1500) member.ID MemberServiceID,member.VisitID ConsumptionVisitID,member.ServiceID ProductID,member.ServicePackageID HeaderServiceID,member.PatientPackageID PurchasedSnapshotID,member.Quantity,member.InPackageQuantity,member.PatientShare,member.CompanyShare,member.PackageShare,member.IsDeleted FROM VisitMgt.VisitService member WHERE member.ServicePackageID IN(SELECT ID FROM VisitMgt.VisitService WHERE VisitID=@VisitID AND EntityID=@EntityID AND VisitServiceClassificationID=8 UNION SELECT ServicePackageID FROM VisitMgt.VisitService WHERE VisitID=@VisitID AND EntityID=@EntityID AND ServicePackageID IS NOT NULL) ORDER BY member.VisitID,member.ID OPTION(MAXDOP 1);

SELECT TOP(1500) b.ID,b.VisitServiceID,b.VisitID,b.ProductID,b.ProductQuantity,b.ProductUOMID,b.EpisodeTypeID,b.ContractID,b.PriceListID,b.Price,b.PatientShare,b.CompanyShare,b.PackageID,b.PatientPackageID,b.PatientPackageDetailID,b.PatientPackageDetailTermID,b.Inquantity,b.PackageShare,b.PackageDiscount,b.Invalid,b.StatusCode,b.IsDeleted FROM Billing.PatientTransaction b WHERE b.ID IN(SELECT BillingTransactionId FROM VisitMgt.VisitService WHERE VisitID=@VisitID AND EntityID=@EntityID) ORDER BY b.ID OPTION(MAXDOP 1);
SELECT TOP(1500) t.ServiceTransactionID,t.TaxID,t.PatientTaxAmount,t.PatientTaxAmountDue,t.CompanyTaxAmount,t.PackageTaxAmount,t.IsDeleted TaxDeleted,s.IsDeleted ServiceDeleted FROM VisitMgt.VisitService s JOIN VisitMgt.ServiceTax t ON t.ServiceTransactionID=s.ID WHERE s.VisitID=@VisitID AND s.EntityID=@EntityID ORDER BY s.ID OPTION(MAXDOP 1);
SELECT TOP(1500) t.PatientTransactionID,t.TaxID,t.TaxAmount,t.TaxAmountDue,t.CompanyTaxAmount,t.PackageTaxAmount,t.IsDeleted FROM Billing.PatientTransactionTax t WHERE t.PatientTransactionID IN(SELECT BillingTransactionId FROM VisitMgt.VisitService WHERE VisitID=@VisitID AND EntityID=@EntityID) OPTION(MAXDOP 1);

-- Verify polymorphic order IDs with classification, product and visit, not ID alone.
SELECT TOP(1500) s.ID VisitServiceID,s.VisitServiceClassificationID,s.OrderlineID,o.ID UnifiedOrderID,o.VisitId UnifiedVisitID,o.ProductId UnifiedProductID,o.ParentId,o.PackageId,m.MedicationOrderLineId,m.TradeId,m.VisitId MedicationVisitID,m.ServiceTransactionID MedicationServiceID FROM VisitMgt.VisitService s LEFT JOIN CPOE.Orders o ON o.ID=s.OrderlineID AND o.VisitId=s.VisitID AND o.ProductId=s.ServiceID AND s.VisitServiceClassificationID<>1 LEFT JOIN CPOE.MedicationOrderLine m ON m.MedicationOrderLineId=s.OrderlineID AND m.TradeId=s.ServiceID AND s.VisitServiceClassificationID=1 WHERE s.VisitID=@VisitID AND s.EntityID=@EntityID ORDER BY s.ID OPTION(MAXDOP 1);
SELECT TOP(1500) OrderLineID,OrderlineTypeID,VisitID,VisitClassificationID,ProductID,ProductCLassificationID,ParentOrderLineId,TotalRequestedQty,TotalChargedQty,TotalAcceptedQty,TotalPerformedQty,TotalDispensedQty FROM VisitMgt.CashedOrderLine WHERE VisitID=@VisitID AND EntityID=@EntityID ORDER BY ID OPTION(MAXDOP 1);
SELECT TOP(1000) i.ID,i.ServiceTransactionID,i.InvoiceID,i.ProductID,i.Quantity,i.PatientShareAmount,i.CompanyShareAmount,i.PackageServiceID,i.PackageInQty,i.PackageShare,i.IsDeleted FROM Finance.InvoiceTransaction i WHERE i.ServiceTransactionID IN(SELECT ID FROM VisitMgt.VisitService WHERE VisitID=@VisitID AND EntityID=@EntityID) ORDER BY i.ID OPTION(MAXDOP 1);
SELECT ID,VisitID,ReceiptID,PaymentMethodID,TransactionTypeID,Amount,IsDeleted,CreatedDate FROM VisitMgt.PaymentTransaction WHERE VisitID=@VisitID AND EntityID=@EntityID ORDER BY ID OPTION(MAXDOP 1);
