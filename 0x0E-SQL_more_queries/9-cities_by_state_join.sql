-- task: Cities by States
SELECT c.id, c.name, s.name 
FROM cities AS c INNER JOIN states AS s 
ON s.id = c.state_id ORDER BY c.id;
