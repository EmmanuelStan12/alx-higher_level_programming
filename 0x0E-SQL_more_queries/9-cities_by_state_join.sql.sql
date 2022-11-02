-- task: Cities by States
SELECT id, name FROM cities INNER JOIN states ON state.id = cities.state_id ORDER BY id;
