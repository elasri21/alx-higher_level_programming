--  lists all cities contained in the database hbtn_0d_usa
SELECT id, name AS tmp_table FROM cities WHERE cities.state_id = states.id
JOIN states.name ON tmp_table ORDER BY cities.id;
