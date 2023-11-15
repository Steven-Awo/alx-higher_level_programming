-- Lists from the hbtn_0d_usa database all the cities in California
-- Lists all the rows of the column in the  database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
