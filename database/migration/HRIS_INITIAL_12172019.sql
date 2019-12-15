-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema hris-db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema hris-db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `hris-db` DEFAULT CHARACTER SET utf8 ;
USE `hris-db` ;

-- -----------------------------------------------------
-- Table `hris-db`.`account`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hris-db`.`account` ;

CREATE TABLE IF NOT EXISTS `hris-db`.`account` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `phone_number` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hris-db`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hris-db`.`user` ;

CREATE TABLE IF NOT EXISTS `hris-db`.`user` (
  `username` VARCHAR(16) NOT NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(32) NOT NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC));


-- -----------------------------------------------------
-- Table `hris-db`.`employee`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hris-db`.`employee` ;

CREATE TABLE IF NOT EXISTS `hris-db`.`employee` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NOT NULL,
  `middle_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(100) NOT NULL,
  `contact_number` VARCHAR(50) NULL,
  `e_mail` VARCHAR(45) NULL,
  `gender` VARCHAR(1) NULL,
  `account_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`, `account_id`, `user_id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `fk_employee_account_idx` (`account_id` ASC),
  INDEX `fk_employee_user1_idx` (`user_id` ASC),
  CONSTRAINT `fk_employee_account`
    FOREIGN KEY (`account_id`)
    REFERENCES `hris-db`.`account` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_employee_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `hris-db`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
