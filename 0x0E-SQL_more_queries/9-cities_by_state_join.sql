-- listing all the cities  that's contained in the hbtn_0d_usa database
-- lists all the rows of the particular column that's in a database
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
