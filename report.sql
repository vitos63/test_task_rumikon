SELECT name, (Positions.salary*Contracts.tax_percentage/100) AS tax_amount 
FROM Employees INNER JOIN Positions ON Employees.position_id = Positions.id
INNER JOIN Contracts ON Contracts.id = Employees.contract_id
WHERE Positions.salary<50000;