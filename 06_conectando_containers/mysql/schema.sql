CREATE DATABASE flaskdocker;
USE flaskdocker;
CREATE TABLE `flaskdocker`.`users` (
	`id` INT PRIMARY KEY NOT NULL  AUTO_INCREMENT,
	`username` VARCHAR(255)
);