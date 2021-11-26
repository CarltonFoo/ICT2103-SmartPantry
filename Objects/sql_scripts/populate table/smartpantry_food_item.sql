-- MariaDB dump 10.17  Distrib 10.4.14-MariaDB, for Win64 (AMD64)
--
-- Host: 127.0.0.1    Database: smartpantry
-- ------------------------------------------------------
-- Server version	10.4.14-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `food_item`
--

DROP TABLE IF EXISTS `food_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `food_item` (
  `fid` int(11) NOT NULL,
  `food_name` varchar(255) NOT NULL,
  `price` float NOT NULL,
  `weight` float NOT NULL,
  `calories` int(11) DEFAULT NULL,
  PRIMARY KEY (`fid`),
  UNIQUE KEY `fid` (`fid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food_item`
--

LOCK TABLES `food_item` WRITE;
/*!40000 ALTER TABLE `food_item` DISABLE KEYS */;
INSERT INTO `food_item` VALUES (1,'Premium Thai Rice',13.75,5000,0),(2,'Ordinary White Bread',1.74,400,0),(3,'Vitamin Enriched Bread',1.63,400,0),(4,'Wholemeal Bread',2.1,400,0),(5,'Lean Pork (Chilled)',15.32,1000,0),(6,'Streaky Pork (Chilled)',17.19,1000,0),(7,'Pork Rib Bones (Chilled)',18.51,1000,0),(8,'Beef (Chilled)',25.18,1000,0),(9,'Mutton (Chilled)',22.03,1000,0),(10,'Whole Chicken (Chilled)',6.32,1000,0),(11,'Chicken Wing (Chilled)',8.43,1000,0),(12,'Duck, Chilled',7.17,1000,0),(13,'Lean Pork (Frozen)',4.9,500,0),(14,'Pork Rib Bones (Frozen)',5.88,500,0),(15,'Cod Fish',65.63,1000,0),(16,'Gold Banded Scad (Kuning)',8.21,1000,0),(17,'Flowery Grouper',13.75,1000,0),(18,'White Pomfret',30.15,1000,0),(19,'Salmon',29.83,1000,0),(20,'Sea Bass',11.7,1000,0),(21,'Sea Bream (Ang Ko Li)',9.93,1000,0),(22,'Golden Snapper',18.79,1000,0),(23,'Spanish Mackerel (Batang)',12.95,1000,0),(24,'Threadfin (Kurau)',60.32,1000,0),(25,'Small Prawns',15.28,1000,0),(26,'Medium Prawns',20.12,1000,0),(27,'Squids',17.72,1000,0),(28,'Infant Milk Powder',6.16,100,0),(29,'Cooking Oil',6.21,2000,0),(30,'Bananas',2.43,1000,0),(31,'Papaya',2.2,1000,0),(32,'Watermelon',1.59,1000,0),(33,'Grapes',11.18,1000,0),(34,'Orange',0.59,0,0),(35,'Apple',0.43,0,0),(36,'Pear',1.28,0,0),(37,'Broccoli',5.7,1000,0),(38,'Cabbage',2.34,1000,0),(39,'Chinese Kale (Kailan)',5.19,1000,0),(40,'Small Mustard (Chye Sim)',3.98,1000,0),(41,'Spinach (Bayam)',3.57,1000,0),(42,'Tomatoes',2.63,1000,0),(43,'Potatoes',2.41,1000,0),(44,'Carrots',2.03,1000,0),(45,'White Sugar',3.08,2000,0),(46,'Instant Coffee',10.19,200,0);
/*!40000 ALTER TABLE `food_item` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-26 16:31:40
