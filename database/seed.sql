-- Seeding exact student and campus data from phpMyAdmin dump
USE `PBLMIA11`;

-- Clear tables prior to seeding
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE `MobilityWish`;
TRUNCATE TABLE `Campus`;
SET FOREIGN_KEY_CHECKS = 1;

-- Load Campus dataset
INSERT INTO `Campus` (`idCampus`, `campusName`) VALUES
(3, 'Douala'),
(4, 'Kinshasa'),
(1, 'Lille'),
(2, 'Nantes'),
(6, 'Paris-Sénart'),
(5, 'Toulouse');

-- Load MobilityWish dataset
INSERT INTO `MobilityWish` (`idMobilityWish`, `studentMail`, `Campus_idCampus`) VALUES
(19, 'céline@icam.fr', 1),
(3, 'david@icam.fr', 1),
(16, 'jean-luc@icam.fr', 2),
(21, 'jean-michel@icam.fr', 2),
(22, 'jean@icam.fr', 3),
(12, 'junie@icam.fr', 1),
(7, 'marie@icam.fr', 1),
(1, 'michel@icam.fr', 1),
(23, 'nicolas@icam.fr', 2),
(2, 'pierre@icam.fr', 2),
(4, 'tanguy@icam.fr', 2);
