-- Cities table
-- script creates thbtn_0d_usa and the cities table in your MySQL server.

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- Create table states
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`id`)
);

-- Create cities table if not existant  
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `state_id` INT NOT NULL,
  `name` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `FK_cities_states` FOREIGN KEY (`state_id`) REFERENCES `hbtn_0d_usa`.`states` (`id`)
);