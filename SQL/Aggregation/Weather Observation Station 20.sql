WITH
    RowNumTable AS (
        SELECT
            LAT_N,
            ROW_NUMBER() OVER (ORDER BY LAT_N) AS row_num
        FROM STATION
    ),
    RowNumMax AS (
        SELECT MAX(row_num)
        FROM RowNumTable
    ),
    TargetIndexes AS (
        SELECT
            LAT_N,
            CASE
                WHEN (
                    (SELECT (SELECT * FROM RowNumMax)) % 2 = 1
                    AND row_num = ((SELECT (SELECT * FROM RowNumMax))+1)/2
                ) THEN 1
                WHEN (
                    (SELECT (SELECT * FROM RowNumMax)) % 2 = 0
                    AND row_num IN (
                        (SELECT (SELECT * FROM RowNumMax))/2,
                        ((SELECT (SELECT * FROM RowNumMax))/2)+1
                    )
                ) THEN 1
                ELSE 0
            END AS row_ind
        FROM RowNumTable
    )

SELECT ROUND(LAT_N, 4)
FROM TargetIndexes
WHERE row_ind = 1

