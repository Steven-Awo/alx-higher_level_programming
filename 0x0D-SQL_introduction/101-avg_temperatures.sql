-- Displays the city's average temperature thats in Fahrenheit in a descending order.
SELECT `city`, AVG(`value`) AS `avge_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
