-- Lists out all the numb of records that has the same score in the table called second_table in our MySQL server.
-- Recordes the counts in a descending order.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
