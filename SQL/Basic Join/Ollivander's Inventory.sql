SELECT W.id, WP.age, W.coins_needed, W.power
FROM Wands W JOIN Wands_Property WP ON W.code=WP.code
WHERE WP.is_evil = 0
    AND W.coins_needed = (SELECT MIN(coins_needed)
                          FROM Wands
                          WHERE power = W.power
                            AND code = W.code)
ORDER BY W.power DESC, WP.age DESC;
