CREATE database if not exists mysql_extracts;
CREATE USER IF NOT EXISTS airbyte_user IDENTIFIED WITH plaintext_password BY 'airbyte_password';
GRANT CREATE, SELECT, INSERT, TRUNCATE ON mysql_extracts.* TO airbyte_user;
GRANT DROP TABLE ON mysql_extracts.* TO airbyte_user;
SELECT version();

CREATE USER IF NOT EXISTS dbt_dev;
CREATE DATABASE IF NOT EXISTS dbt_dev;
SHOW users;

SHOW tables in mysql_extracts;