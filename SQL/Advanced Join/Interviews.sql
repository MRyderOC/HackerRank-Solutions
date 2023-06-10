-- MS SQL Query
WITH
    StatsGrouped AS (
        SELECT
            challenge_id,
            SUM(total_views) AS sum_views,
            SUM(total_unique_views) AS sum_unique_views
        FROM View_Stats
        GROUP BY challenge_id
    ),
    SubmissionsGrouped AS (
        SELECT
            challenge_id,
            SUM(total_submissions) AS sum_submissions,
            SUM(total_accepted_submissions) AS sum_accepted_submissions
        FROM Submission_Stats
        GROUP BY challenge_id
    ),
    StatsCollegeSums AS (
        SELECT
            Challenges.college_id AS college_id,
            SUM(sum_views) AS sum_views,
            SUM(sum_unique_views) AS sum_unique_views
        FROM StatsGrouped
        LEFT JOIN Challenges ON
            Challenges.challenge_id = StatsGrouped.challenge_id
        GROUP BY college_id
    ),
    SubsCollegeSums AS (
        SELECT
            Challenges.college_id AS college_id,
            SUM(sum_submissions) AS sum_submissions,
            SUM(sum_accepted_submissions) AS sum_accepted_submissions
        FROM SubmissionsGrouped
        LEFT JOIN Challenges ON
            Challenges.challenge_id = SubmissionsGrouped.challenge_id
        GROUP BY college_id
    ),
    StatsContentsSums AS (
        SELECT
            Colleges.contest_id AS contest_id,
            SUM(sum_views) AS sum_views,
            SUM(sum_unique_views) AS sum_unique_views
        FROM StatsCollegeSums
        LEFT JOIN Colleges ON
            Colleges.college_id = StatsCollegeSums.college_id
        GROUP BY contest_id
    ),
    SubsContentsSums AS (
        SELECT
            Colleges.contest_id AS contest_id,
            SUM(sum_submissions) AS sum_submissions,
            SUM(sum_accepted_submissions) AS sum_accepted_submissions
        FROM SubsCollegeSums
        LEFT JOIN Colleges ON
            Colleges.college_id = SubsCollegeSums.college_id
        GROUP BY contest_id
    ),

    ResultTable AS (
        SELECT
            Contests.contest_id, hacker_id, name,
            sum_submissions,
            sum_accepted_submissions,
            sum_views,
            sum_unique_views
        FROM Contests
        RIGHT JOIN StatsContentsSums ON
            Contests.contest_id = StatsContentsSums.contest_id
        RIGHT JOIN SubsContentsSums ON
            Contests.contest_id = SubsContentsSums.contest_id
        WHERE
            sum_submissions <> 0 AND
            sum_accepted_submissions <> 0 AND
            sum_views <> 0 AND
            sum_unique_views <> 0
    )

SELECT *
FROM ResultTable
ORDER BY contest_id;
