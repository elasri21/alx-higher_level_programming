--  lists all cities contained in the database hbtn_0d_usa
SELECT id, name FROM cities WHERE cities.state_id = states.id
JOIN ON states.name ORDER BY cities.id;
