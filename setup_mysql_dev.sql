-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS plaza_dev_db;
CREATE USER IF NOT EXISTS 'plaza_dev'@'localhost' IDENTIFIED BY 'plaza_dev_pwd';
GRANT ALL PRIVILEGES ON `plaza_dev_db`.* TO 'plaza_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'plaza_dev'@'localhost';
FLUSH PRIVILEGES;
