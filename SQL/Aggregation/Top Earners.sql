SELECT MAX(salary * months), 
    (SELECT COUNT(*)
     FROM Employee
     WHERE salary * months = (SELECT MAX(salary * months)
                              FROM Employee
     )
    )
FROM Employee;
