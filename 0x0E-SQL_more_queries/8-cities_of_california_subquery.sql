-- lists all the cities of California that can be found in the database
SELECT id, name FROM cities WHERE states.name='California'
AND cities.state_id = states.id ORDER BY cities.id;
