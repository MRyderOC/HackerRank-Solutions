SELECT C.hacker_id, H.name, COUNT(C.challenge_id) AS c_count
FROM Challenges C JOIN Hackers H ON H.hacker_id=C.hacker_id
GROUP BY C.hacker_id, H.name
HAVING c_count = (SELECT MAX(tmp.inner_count)
                  FROM (SELECT COUNT(challenge_id) AS inner_count FROM Challenges GROUP BY hacker_id) tmp)
    OR c_count IN (SELECT tmp2.inner_count
                   FROM (SELECT COUNT(challenge_id) AS inner_count FROM Challenges GROUP BY hacker_id) tmp2
                   GROUP BY tmp2.inner_count
                   HAVING COUNT(tmp2.inner_count) = 1)
ORDER BY c_count DESC, C.hacker_id;
