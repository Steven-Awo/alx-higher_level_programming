-- Creates the database called hbtn_0d_usa and also the table called states with values on my MySQL server
-- Creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Uses the databas hbtn_0d_usa
USE hbtn_0d_usa;
-- Creates a table with id and other variables
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
