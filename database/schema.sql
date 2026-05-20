-- Database Schema: PBLMIA11 (Match exact school phpMyAdmin dump)
CREATE DATABASE IF NOT EXISTS `PBLMIA11` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `PBLMIA11`;

-- Drop tables if they exist to refresh structure
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS `MobilityWish`;
DROP TABLE IF EXISTS `Campus`;
SET FOREIGN_KEY_CHECKS = 1;

-- Table structure for table `Campus`
CREATE TABLE `Campus` (
  `idCampus` int(11) NOT NULL AUTO_INCREMENT,
  `campusName` varchar(45) NOT NULL,
  PRIMARY KEY (`idCampus`),
  UNIQUE KEY `campusName_UNIQUE` (`campusName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Table structure for table `MobilityWish`
CREATE TABLE `MobilityWish` (
  `idMobilityWish` int(11) NOT NULL AUTO_INCREMENT,
  `studentMail` varchar(45) NOT NULL,
  `Campus_idCampus` int(11) NOT NULL,
  PRIMARY KEY (`idMobilityWish`,`Campus_idCampus`),
  UNIQUE KEY `studentMail_UNIQUE` (`studentMail`),
  KEY `fk_MobilityWish_Campus_idx` (`Campus_idCampus`),
  CONSTRAINT `fk_MobilityWish_Campus` FOREIGN KEY (`Campus_idCampus`) REFERENCES `Campus` (`idCampus`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
