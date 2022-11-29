/* Zlaczenia jednokrotne */
SELECT Products.ProductName , Suppliers.CompanyName FROM Products INNER JOIN Suppliers ON Products.SupplierID=Suppliers.SupplierID

SELECT DISTINCT Customers.CompanyName FROM Customers INNER JOIN Orders ON Customers.CustomerID=Orders.CustomerID WHERE Customers.City!=Orders.ShipCity

SELECT Employees.FirstName as 'Imie szef', Employees.LastName as 'Nazwisko szef', Druga.LastName as 'Nazwsiko pracownik',Druga.FirstName as 'Imie pracownik' FROM Employees INNER JOIN Employees as Druga ON Employees.EmployeeID=Druga.ReportsTo 

/* Zlaczenia wielokrotne */
SELECT Products.ProductName,Orders.OrderID FROM Products INNER JOIN [Order Details] ON Products.ProductID=[Order Details].ProductID INNER JOIN Orders ON Orders.OrderID=[Order Details].OrderID WHERE [Order Details].Quantity>100

SELECT DISTINCT Employees.FirstName,Employees.LastName FROM Employees INNER JOIN Orders ON Orders.EmployeeID=Employees.EmployeeID INNER JOIN [Order Details] ON [Order Details].OrderID=Orders.OrderID INNER JOIN Products ON Products.ProductID=[Order Details].ProductID WHERE Products.ProductName='Tofu'

SELECT DISTINCT Customers.CompanyName FROM Customers INNER JOIN Orders ON Orders.CustomerID=Customers.CustomerID INNER JOIN Employees ON Employees.EmployeeID=Orders.EmployeeID WHERE Employees.FirstName='Steven' AND Employees.LastName='Buchanan'

/* Wyliczenia na zlaczeniach */
SELECT  DISTINCT COUNT(Orders.EmployeeID) OVER (PARTITION BY Orders.EmployeeID) as 'Ilosc zamowien', Employees.FirstName, Employees.LastName FROM Employees INNER JOIN Orders ON Orders.EmployeeID=Employees.EmployeeID

SELECT DISTINCT Customers.CompanyName, SUM([Order Details].Quantity*[Order Details].UnitPrice) OVER (PARTITION BY Customers.CustomerID) FROM [Order Details] INNER JOIN Orders ON Orders.OrderID=[Order Details].OrderID INNER JOIN Customers ON Customers.CustomerID=Orders.CustomerID

SELECT TOP 5 Employees.FirstName,Employees.LastName,[Order Details].Discount FROM Employees INNER JOIN Orders ON Orders.EmployeeID=Employees.EmployeeID INNER JOIN [Order Details] ON [Order Details].OrderID=Orders.OrderID  ORDER BY [Order Details].Discount DESC 

SELECT DISTINCT Employees.FirstName,Employees.LastName,AVG([Order Details].Quantity*[Order Details].UnitPrice)  OVER (PARTITION BY Employees.EmployeeID) as 'SREDNIA',MAX([Order Details].Quantity*[Order Details].UnitPrice)  OVER (PARTITION BY Employees.EmployeeID) as 'MAX',MIN([Order Details].Quantity*[Order Details].UnitPrice)  OVER (PARTITION BY Employees.EmployeeID) as 'MIN' FROM Employees INNER JOIN Orders ON Orders.EmployeeID=Employees.EmployeeID INNER JOIN [Order Details] ON [Order Details].OrderID=Orders.OrderID

SELECT
    COALESCE(Employees.ReportsTo, 0) AS Szefowie, SUM([Order Details].UnitPrice * [Order Details].Quantity * [Order Details].Discount) AS suma_rabatow
FROM
    Employees
RIGHT JOIN
    Orders
ON
    Orders.EmployeeID = Employees.EmployeeID
LEFT JOIN
    [Order Details]
ON
    Orders.OrderID = [Order Details].OrderID
GROUP BY
    Employees.ReportsTo
ORDER BY
    Szefowie
