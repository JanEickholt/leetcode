SELECT customers.name as Customers
FROM Customers
LEFT JOIN Orders
ON Orders.customerId = Customers.id
WHERE Orders.customerId is Null
