-- Lists all the cities of California that can be found
SELECT * FROM cities WHERE state_id = (SELECT id from states WHERE name = 'California');
