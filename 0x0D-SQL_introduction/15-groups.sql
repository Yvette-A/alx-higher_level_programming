-- lists the number of records with the same score
SELECT score, COUNT(id) AS number
FROM second_table
GROUP BY score
ORDER BY COUNT(id) DESC;
