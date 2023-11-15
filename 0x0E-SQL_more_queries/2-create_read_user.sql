-- creates a database for hbtn_0d_2 and for the user user_0d_2
-- creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creates a new user hbtn_0d_2
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- grants all the SELECT the privileges to a user
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
