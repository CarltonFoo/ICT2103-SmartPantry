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
-- Table structure for table `receipt_ingredient`
--

DROP TABLE IF EXISTS `receipt_ingredient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `receipt_ingredient` (
  `receipt_id` int(11) NOT NULL,
  `fid` int(11) NOT NULL,
  `weight` float NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`receipt_id`,`fid`),
  KEY `fid` (`fid`),
  CONSTRAINT `receipt_ingredient_ibfk_1` FOREIGN KEY (`receipt_id`) REFERENCES `receipt` (`receipt_id`),
  CONSTRAINT `receipt_ingredient_ibfk_2` FOREIGN KEY (`fid`) REFERENCES `food_item` (`fid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receipt_ingredient`
--

LOCK TABLES `receipt_ingredient` WRITE;
/*!40000 ALTER TABLE `receipt_ingredient` DISABLE KEYS */;
INSERT INTO `receipt_ingredient` VALUES (1,1,5000,'2021-09-26'),(1,3,400,'2021-09-26'),(1,4,400,'2021-09-26'),(1,5,1000,'2021-09-26'),(1,6,1000,'2021-09-26'),(2,1,5000,'2021-10-26'),(2,2,400,'2021-10-26'),(3,6,1000,'2021-11-26'),(3,7,1000,'2021-11-26'),(3,8,1000,'2021-11-26'),(3,9,1000,'2021-11-26');
/*!40000 ALTER TABLE `receipt_ingredient` ENABLE KEYS */;
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
