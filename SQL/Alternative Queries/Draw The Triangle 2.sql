DELIMITER $$

CREATE PROCEDURE pr_pattern2()
BEGIN
    DECLARE i INT DEFAULT 1;

    WHILE i <= 20 DO
        SELECT REPEAT('* ', i);
        SET i = i + 1;
    END WHILE;

END $$
DELIMITER ;


CALL pr_pattern2();
