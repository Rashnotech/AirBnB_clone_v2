-- Prepares a MySQL server
-- create a database hbnb_test_db

CREATE DATABASE IF NOT EXISTS hbnb_test_db;

USE hbnb_test_db;

-- create a user and identify with password
CREATE USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant all permission to hbnb_test on hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost' WITH GRANT OPTION;

-- grant select privilege to database performance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost'
