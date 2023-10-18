-- this script creates the database hbtn_0d_usa
-- with a table cities on my MYSQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	FOREIGN KEY (id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);
