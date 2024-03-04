-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS plaza_test_db;
CREATE USER IF NOT EXISTS 'plaza_test'@'localhost' IDENTIFIED BY 'plaza_test_pass';
GRANT ALL PRIVILEGES ON `plaza_test_db`.* TO 'plaza_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'plaza_test'@'localhost';
FLUSH PRIVILEGES;
