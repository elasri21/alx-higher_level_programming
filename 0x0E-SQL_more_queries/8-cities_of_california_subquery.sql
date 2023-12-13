-- lists all the cities of California that can be found in the database
SELECT * FROM cities WHERE states.name='California' ORDER BY cities.id;
