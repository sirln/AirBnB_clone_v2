-- Creation of a MySql Server with the following info:
-- A database named hbnb_test_db
-- Username: hbnb_test (in localhost), Password: hbnb_test_pwd
-- Grants all privileges for hbnb_test on hbnb_test_db
-- Grants SELECT privilege for hbnb_test on performance_schema
-- Flush Privileges (Reloads the grant tables' privileges)

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER
  IF NOT EXISTS "hbnb_test"@"localhost"
  IDENTIFIED BY "hbnb_test_pwd";
GRANT ALL PRIVILEGES
  ON `hbnb_test_db`.*
  TO "hbnb_test"@"localhost";
GRANT SELECT
  ON `performance_schema`.*
  TO "hbnb_test"@"localhost";
FLUSH PRIVILEGES;
