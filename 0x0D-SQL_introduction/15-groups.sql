-- This query lists the number of records with the same score in the table second_table in the MySQL server.
-- The result set is grouped by the score column, and the count of records for each score is calculated.
-- The result is then ordered in descending order based on the count.

SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
