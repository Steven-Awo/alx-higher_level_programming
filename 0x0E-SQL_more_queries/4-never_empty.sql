-- creates the table called id_not_null if not avaliable on our MySQL server
-- creates a new table
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
