-- Lists the number of records with the same score in the table second_table
-- Result displays score and the number of records (label: number)
-- Sorted by the number of records (descending)
SELECT score, COUNT(*) AS number 
FROM second_table 
GROUP BY score 
ORDER BY number DESC;
