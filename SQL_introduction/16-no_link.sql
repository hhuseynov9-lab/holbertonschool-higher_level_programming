-- Lists all records of the table second_table
-- Don't list rows where the name column does not contain a value
-- Results display the score and the name, ordered by score (top first)
SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL AND name <> ''
ORDER BY score DESC;
