SHOW variables LIKE "log_bin";

SELECT VERSION(); 

CREATE USER IF NOT EXISTS 'airbyte'@'%' IDENTIFIED BY 'your_password_here';

GRANT SELECT ON visit.* TO 'airbyte'@'%';

GRANT SELECT, RELOAD, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'airbyte'@'%';