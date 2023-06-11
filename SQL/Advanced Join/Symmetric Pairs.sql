WITH
    SelfJoinTable AS (
        SELECT
            F1.X AS X1, F1.Y AS Y1,
            F2.X AS X2, F2.Y AS Y2
        FROM Functions AS F1
        CROSS JOIN Functions AS F2
    ),
    OddCountOfEqualPairs AS (
        SELECT X
        FROM Functions
        WHERE X = Y
        GROUP BY X
        HAVING COUNT(X) % 2 = 0
    ),
    SymmetricPairsHelper AS (
        SELECT
            X1, Y1,
            CASE
                WHEN X1 != Y1 THEN 1
                WHEN (
                    X1 = Y1 AND
                    X1 IN (SELECT * FROM OddCountOfEqualPairs)
                ) THEN 1
                ELSE 0
            END AS IS_VALID
        FROM SelfJoinTable
        WHERE X1 = Y2 AND X2 = Y1
    ),
    ResultHelper AS (
        SELECT DISTINCT X1, Y1
        FROM SymmetricPairsHelper
        WHERE IS_VALID = 1 AND X1 <= Y1
    )


SELECT *
FROM ResultHelper
ORDER BY X1, Y1;
