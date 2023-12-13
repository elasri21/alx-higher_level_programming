-- lists all the cities of California that can be found in the database
SELECT * FROM cities WHERE cities.state_id = states.id
AND states.name='California' ORDER BY cities.id;
