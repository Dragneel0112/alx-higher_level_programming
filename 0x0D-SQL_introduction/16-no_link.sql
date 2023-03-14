-- Lists all records in second_table except those with no name value
-- Database passed as argument in mysql
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
