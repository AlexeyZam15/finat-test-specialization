DROP DATABASE IF EXISTS man_friends_db;
CREATE DATABASE man_friends_db;
USE man_friends_db;

DROP TABLE IF EXISTS parent_class;
CREATE TABLE parent_class (
	Id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    birthday DATE,
    class_name VARCHAR(50),
    breed VARCHAR(50),
    learned_commands VARCHAR(120)
);
