
CREATE SCHEMA IF NOT EXISTS `library` DEFAULT CHARACTER SET utf8 ;
USE `library` ;

-- -----------------------------------------------------
-- Table `library`.`book`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `library`.`book` (
  `idbook` INT NOT NULL auto_increment,
  `title` VARCHAR(45) NULL,
  `author` VARCHAR(45) NULL,
  `language` VARCHAR(45) NULL,
  `code` VARCHAR(45) NULL,
  `grade` VARCHAR(45) NULL,
  `section` VARCHAR(45) NULL,
  `description` VARCHAR(45) NULL,
  `physical_state` VARCHAR(45) NULL,
  `quantity` INT NULL,
  `stock` INT NULL,
  `status` tinyint not null default 1,
  PRIMARY KEY (`idbook`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `library`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `library`.`user` (
  `iduser` INT NOT NULL auto_increment,
  `user_name` VARCHAR(45) NULL,
  `user_last_name` VARCHAR(45) NULL,
  `mail` VARCHAR(45) NULL,
  `role` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  `grade` VARCHAR(45) NULL,
  `status` tinyint not null default 1,
  PRIMARY KEY (`iduser`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `library`.`loan`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `library`.`loan` (
  `idloan` INT NOT NULL auto_increment,
  `acquisition_date` DATE NULL,
  `date_of_devolution` DATE NULL,
  `book_idbook` INT NOT NULL,
  `user_iduser` INT NOT NULL,
  `confirm_devolution` TINYINT NULL,
  PRIMARY KEY (`idloan`, `book_idbook`, `user_iduser`),
  INDEX `fk_loan_book_idx` (`book_idbook` ASC) ,
  INDEX `fk_loan_user1_idx` (`user_iduser` ASC) ,
  CONSTRAINT `fk_loan_book`
    FOREIGN KEY (`book_idbook`)
    REFERENCES `library`.`book` (`idbook`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_loan_user1`
    FOREIGN KEY (`user_iduser`)
    REFERENCES `library`.`user` (`iduser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;




