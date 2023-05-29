WITH
  HelperTable AS (
    SELECT
        *, LAG(End_Date) OVER() AS Last_End_Date
    FROM Projects
    ORDER BY Start_Date
  ),
  NewTaskFinder AS (
    SELECT
        *,
        CASE
            WHEN Start_Date = Last_End_Date THEN FALSE
            ELSE TRUE
        END AS Is_New_Task
    FROM HelperTable      
  ),
  TaskStartEndDates AS (
    SELECT
        Start_Date,
        LEAD(Last_End_Date, 1, End_Date) OVER() AS End_D
    FROM NewTaskFinder
    WHERE Is_New_Task = 1
  ),
  TaskStartEndDatesWithDiff AS (
    SELECT
        Start_Date, End_D,
        DATEDIFF(End_D, Start_Date) AS Dif_Date
    FROM TaskStartEndDates
  )

SELECT
  Start_Date, End_D
FROM TaskStartEndDatesWithDiff
ORDER BY Dif_Date, Start_Date;
