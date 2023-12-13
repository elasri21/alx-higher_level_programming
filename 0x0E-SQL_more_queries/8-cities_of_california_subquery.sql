-- lists all the cities of California that can be found in the database
SELECT * FROM cities WHERE cities.states_d = states.id
AND states.name='California' ORDER BY cities.id;
