-- Lists all the records that are in the table called second_table with the score >= 10 in our MySQL server.
-- Records the score in a descending order..
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
