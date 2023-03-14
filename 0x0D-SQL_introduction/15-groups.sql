-- Lists the number of records with the same score from second_table
-- Database passed as argument in mysql
SELECT score, COUNT('score') as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
