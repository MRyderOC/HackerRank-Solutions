DELIMITER $$

CREATE PROCEDURE prime_nums()
BEGIN
    DECLARE i INT DEFAULT 2;
    DECLARE dev INT;
    DECLARE is_prime BOOLEAN;
    DECLARE nums_string VARCHAR(1000);

    WHILE i <= 1000 DO
        SET dev = 2;
        SET is_prime = TRUE;

        inner_loop: WHILE dev < i DO
            IF MOD(i, dev) = 0 THEN
                SET is_prime = FALSE;
                LEAVE inner_loop;
            END IF;
            SET dev = dev + 1;
        END WHILE;

        IF is_prime = TRUE THEN
            SET nums_string = CONCAT_WS('&', nums_string, i);
        END IF;

        SET i = i + 1;
    END WHILE;

    SELECT nums_string;

END $$

DELIMITER ;


CALL prime_nums();
