SELECT H.hacker_id, H.name
FROM Submissions S
  JOIN Challenges C ON C.challenge_id=S.challenge_id
  JOIN Hackers H ON H.hacker_id=S.hacker_id
  JOIN Difficulty D ON D.difficulty_level=C.difficulty_level
WHERE S.score = D.score
  AND D.difficulty_level = C.difficulty_level
GROUP BY H.hacker_id, H.name
HAVING COUNT(S.challenge_id) > 1
ORDER BY COUNT(S.challenge_id) DESC, H.hacker_id ASC;
