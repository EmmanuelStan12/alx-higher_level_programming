-- List all the number of records with the same score
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
