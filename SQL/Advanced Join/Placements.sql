WITH
    FriendsTable AS (
        SELECT
            Students.ID AS Student_ID,
            Students.Name AS Student_Name,
            Friend_ID
        FROM Students LEFT JOIN Friends ON Students.ID = Friends.ID
    ),
    WithStudentSalary AS (
        SELECT
            Student_ID, Student_Name, Friend_ID,
            Packages.Salary AS Student_Salary
        FROM FriendsTable LEFT JOIN Packages ON FriendsTable.Student_ID = Packages.ID
    ),
    WithSalary AS (
        SELECT
            Student_ID, Student_Name, Friend_ID, Student_Salary,
            Packages.Salary AS Friend_Salary
        FROM WithStudentSalary LEFT JOIN Packages ON WithStudentSalary.Friend_ID = Packages.ID
    )


SELECT Student_Name
FROM WithSalary
WHERE Friend_Salary > Student_Salary
ORDER BY Friend_Salary;
