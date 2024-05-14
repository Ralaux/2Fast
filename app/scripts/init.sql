SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+01:00";

USE 2Fast;

DROP TABLE IF EXISTS `characters`;
CREATE TABLE `characters` (
    `char_id` int auto_increment primary key not null, 
    `classe` varchar(100) not null, 
    `nom` varchar(255) not null, 
    `serveur` varchar(100) not null, 
    `isdeleted` boolean,
    `creation_date` DATETIME, 
    `modification_date` DATETIME
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `stats`;
CREATE TABLE `stats` (
  `stat_id` int auto_increment primary key not null,
  `char_id` int NOT NULL,
  `agilité` int NOT NULL,
  `force` int NOT NULL,
  `chance` int NOT NULL,
  `intelligence` int NOT NULL,
  FOREIGN KEY (`char_id`) REFERENCES `characters`(`char_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

INSERT INTO characters (nom, classe, serveur, isdeleted, creation_date, modification_date) VALUES ("Zoelhya", "eliotrope", "Tylezia", false, Now(), Now());
INSERT INTO characters (nom, classe, serveur, isdeleted, creation_date, modification_date) VALUES ("Cataliama", "cra", "Tylezia", false, Now(), Now());
INSERT INTO characters (nom, classe, serveur, isdeleted, creation_date, modification_date) VALUES ("Palancar", "eniripsa", "Tylezia", false, Now(), Now());
