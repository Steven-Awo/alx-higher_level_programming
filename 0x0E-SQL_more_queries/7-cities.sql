-- Creates a new database called hbtn_0d_usa and a table called cities in the hbtn_0d_usa database on my MySQL server
-- Creates a new database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Uses the database hbtn_0d_usa
USE hbtn_0d_usa;
-- Creates a table with values
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(state_id) REFERENCES states(id));
