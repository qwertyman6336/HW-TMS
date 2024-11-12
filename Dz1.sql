CREATE TABLE Employees (
    Name VARCHAR(100),
    Position VARCHAR(100),
    Department VARCHAR(100),
    Salary DECIMAL(10, 2)
);

INSERT INTO Employees (Name, Position, Department, Salary) VALUES
('Alice Smith', 'Developer', 'IT', 6000),
('Bob Johnson', 'Manager', 'Sales', 8000),
('Charlie Brown', 'Developer', 'IT', 5500),
('Diana Prince', 'Sales Associate', 'Sales', 4000);

UPDATE Employees
SET Position = 'Senior Developer'
WHERE Name = 'Alice Smith';


ALTER TABLE Employees
ADD HireDate DATE;

UPDATE Employees
SET HireDate = '2021-01-15'
WHERE Name = 'Alice Smith';

UPDATE Employees
SET HireDate = '2020-03-22'
WHERE Name = 'Bob Johnson';

UPDATE Employees
SET HireDate = '2021-06-10'
WHERE Name = 'Charlie Brown';

UPDATE Employees
SET HireDate = '2022-02-01'
WHERE Name = 'Diana Prince';

SELECT * FROM Employees
WHERE Position = 'Manager';

SELECT * FROM Employees
WHERE Salary > 5000;

SELECT * FROM Employees
WHERE Department = 'Sales';

SELECT AVG(Salary) AS AverageSalary FROM Employees;

--DROP TABLE Employees;
