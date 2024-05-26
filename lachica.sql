CREATE DATABASE  IF NOT EXISTS `shoes` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;
USE `shoes`;
-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: shoes
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `shoe`
--

DROP TABLE IF EXISTS `shoe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `shoe` (
  `shoesID` varchar(5) NOT NULL,
  `shoesname` varchar(45) NOT NULL,
  PRIMARY KEY (`shoesID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoe`
--

LOCK TABLES `shoe` WRITE;
/*!40000 ALTER TABLE `shoe` DISABLE KEYS */;
INSERT INTO `shoe` VALUES ('02','Nike Air Max 270'),('03','Nike Air Max 90'),('04','Nike Air Zoom Pegasus 37'),('05','Nike Air VaporMax'),('06','Nike Air Max 97'),('07','Adidas Ultraboost'),('08','Reebok Classic'),('09','Puma Suede'),('10','New Balance 574'),('11','Converse All Star'),('12','ASICS Gel-Kayano'),('13','Vans Old Skool'),('14','Saucony Jazz'),('15','Mizuno Wave Rider'),('16','Hoka One One Clifton'),('17','Under Armour HOVR'),('18','Brooks Ghost'),('19','Skechers GoWalk'),('20','Fila Disruptor'),('21','Jordan Air 1'),('22','Nike React'),('23','Adidas NMD'),('24','Reebok Pump'),('25','Puma Ignite');
/*!40000 ALTER TABLE `shoe` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-27  4:09:28
