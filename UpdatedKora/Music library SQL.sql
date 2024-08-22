CREATE DATABASE  IF NOT EXISTS `musiclibrary` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `musiclibrary`;
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: musiclibrary
-- ------------------------------------------------------
-- Server version	9.0.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `playlistoperations`
--

DROP TABLE IF EXISTS `playlistoperations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `playlistoperations` (
  `OperationID` int NOT NULL AUTO_INCREMENT,
  `PlaylistID` int NOT NULL,
  `SongID` int NOT NULL,
  PRIMARY KEY (`OperationID`),
  KEY `PlaylistID` (`PlaylistID`),
  KEY `SongID` (`SongID`),
  CONSTRAINT `playlistoperations_ibfk_1` FOREIGN KEY (`PlaylistID`) REFERENCES `playlists` (`PlaylistID`) ON DELETE CASCADE,
  CONSTRAINT `playlistoperations_ibfk_2` FOREIGN KEY (`SongID`) REFERENCES `songs` (`SongID`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `playlistoperations`
--

LOCK TABLES `playlistoperations` WRITE;
/*!40000 ALTER TABLE `playlistoperations` DISABLE KEYS */;
INSERT INTO `playlistoperations` VALUES (2,1,4),(3,1,9);
/*!40000 ALTER TABLE `playlistoperations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `playlists`
--

DROP TABLE IF EXISTS `playlists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `playlists` (
  `PlaylistID` int NOT NULL AUTO_INCREMENT,
  `PlaylistName` varchar(100) DEFAULT NULL,
  `Description` text,
  PRIMARY KEY (`PlaylistID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `playlists`
--

LOCK TABLES `playlists` WRITE;
/*!40000 ALTER TABLE `playlists` DISABLE KEYS */;
INSERT INTO `playlists` VALUES (1,'tino','testing play');
/*!40000 ALTER TABLE `playlists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `songs`
--

DROP TABLE IF EXISTS `songs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `songs` (
  `SongID` int NOT NULL AUTO_INCREMENT,
  `SongName` varchar(255) DEFAULT NULL,
  `Artist` varchar(255) DEFAULT NULL,
  `Genre` varchar(255) DEFAULT NULL,
  `Mood` varchar(50) DEFAULT NULL,
  `Year_of_Release` int DEFAULT NULL,
  `YouTubeURL` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`SongID`)
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `songs`
--

LOCK TABLES `songs` WRITE;
/*!40000 ALTER TABLE `songs` DISABLE KEYS */;
INSERT INTO `songs` VALUES (2,'Jazz (We\'ve Got)','A Tribe Called Quest','HipHop','Energising',1991,'Jazz (We\'ve Got)'),(3,'Giant Steps','John Coltrane','Jazz','Energising',1960,'Giant Steps'),(4,'Full OST','Stray Game | Full OST','Game OST','Chill',2022,'Stray Game | Full OST'),(5,'Nothing That Has Happened So Far Has Been Anything That We Could Control','Tame Impala','Indie','Energising',2012,'Nothing That Has Happened So Far Has Been Anything That We Could Control'),(6,'Arabesque No. 1','Claude Debussy','Classical','Chill',1888,'Arabesque No. 1'),(7,'DELTA Waves [3Hz]','Sleeptube - Hyponotic Relaxation','Ambient','Chill',2024,'DELTA Waves [3Hz]'),(8,'Guess','Charlie xcx - ft. Billie Eilish','Pop','Energising',2024,'Guess'),(9,'Circles','Adam F','Drum & Bass','Energising',1997,'Circles'),(10,'Maddest Crew','Machel Montano','Soca','Energising',2022,'Maddest Crew'),(11,'Brown Paper Bag','Roni Size','Jungle','Energising',1997,'Brown Paper Bag'),(12,'Ponyboy','Sophie','Electronic','Energising',2018,'Ponyboy'),(13,'Meadowlarks','Fleet Foxes','Folk','Chill',2008,'Meadowlarks'),(14,'Jump (ft. Swizz Beatz)','Elephant Man','Dancehall','Energising',2008,'Jump'),(15,'Water No Get Enemy','Fela Kuti','Afrobeats','Energising',1975,'Water No Get Enemy'),(16,'Windowlicker','Aphex Twin','Hardcore / Breakcore / Breakbeats','Energising',1999,'Windowlicker'),(17,'Y2K TECHNO DJ MIX','dedeco /// VGM DJ','DJ Mixes','Energising',2023,'Y2K TECHNO DJ MIX'),(18,'Beychella (Live from Coachella Valley Music & Arts Festival 2018) [Remastered 60FPS]','Beyonce\'s Beychella','Live Performances','Energising',2018,'Beychella 2018'),(19,'Tron Song','Thundercat','Alternative','Chill',2013,'Tron Song'),(21,'Sing About Me, I\'m Dying of Thirst','Kendrick Lamar','HipHop','Chill',2012,'Sing About Me, I\'m Dying of Thirst'),(22,'Askim','Kamasi Washington','Jazz','Chill',2015,'Askim'),(23,'Gris OST','Gris','Game OST','Chill',2021,'Gris OST'),(24,'Odelay - Full Album','Beck','Indie','Energising',1996,'Odelay - Full Album'),(25,'Best of Dvořák - Essential Classical Music','Antonin Dvořák','Classical','Chill',2004,'Best of Dvořák - Essential Classical Music'),(26,'Ambient Buddhism','Takeo Suzuki','Ambient','Chill',2024,'Ambient Buddhism'),(27,'Wannabe','Spice Girls','Pop','Energising',1996,'Wannabe'),(28,'Tekken | Ambient DnB','jungletone.','Drum & Bass','Energising',2024,'Tekken | Ambient DnB'),(29,'Soca 2024 Summer Mix','ScottchBonnet','Soca','Energising',2024,'Soca 2024 Summer Mix'),(30,'MixMag: The Lab LDN','DJ Randall','Jungle','Energising',2016,'MixMag: The Lab LDN'),(31,'Pluto','Bjork','Electronic','Energising',1997,'Pluto'),(32,'Tranquillitas','NUMA','Folk','Chill',2019,'Tranquillitas'),(33,'Hit & Run, ft. Masicka, Di Genius','Shenseea','Dancehall','Energising',2024,'Hit & Run, ft. Masicka, Di Genius'),(34,'African Giant - Live from London (YouTube Live Stream)','Burna Boy','Afrobeats','Energising',2024,'African Giant - Live from London (YouTube Live Stream)'),(35,'90\'s Breakbeat Vinyl Mix','Hebbs','Hardcore / Breakcore / Breakbeats','Energising',2015,'90s Breakbeat Vinyl Mix'),(36,'Boiler Room Palestine','Sama\' Abdulhadi','DJ Mixes','Energising',2019,'Boiler Room Palestine'),(37,'Live Concert - 2021','Constantinople / Kiya Tabassian, Ablaye Cissoko, Patrick Graham / TRAVERSÉES','Live Performances','Chill',2021,'Full Concert - 2021'),(38,'So Many Details','Toro y Moi','Alternative','Chill',2012,'So Many Details'),(39,'I\'m That Girl','Beyonce','R\'n\'B','Energising',2022,'I\'m That Girl'),(40,'The Boy is a Gun','Tyler, The Creator','HipHop','Chill',2019,'Boy Is A Gun'),(41,'Godzilla','Vels Trio','Jazz','Energising',2017,'Godzilla'),(42,'[Official] TUNIC (Original Soundtrack)','Tunic - OST','Game OST','Chill',2022,'[Official] TUNIC (Original Soundtrack)'),(43,'Oh Detroit, Lift Up Your Weary Head!','Sufjan Stevens','Indie','Chill',2003,'Oh Detroit, Lift Up Your Weary Head!'),(44,'Classical Music for Reading','HALIDONMUSIC','Classical','Chill',2018,'Classical Music for Reading'),(45,'Until the Quiet Comes - Full Album (Playlist)','Flying Lotus','Ambient','Energising',2012,'Until the Quiet Comes - Full Album (Playlist)'),(46,'St. Vincent - Full Album Playlist','St. Vincent','Pop','Energising',2013,'St. Vincent - Full Album (Playlist)'),(47,'Oldschool Atmospheric Jungle DnB Sesh','[mystery]','Drum & Bass','Energising',2024,'Oldschool Atmospheric Jungle DnB Sesh'),(48,'Miss Daisy','Peter Humphrey','Soca','Energising',1994,'Miss Daisy'),(49,'Digital (2008 Re-Edit)','Roni Size','Jungle','Energising',2008,'Digital (2008 - Re-Edit)'),(50,'Family','Bjork','Electronic','Chill',2015,'Family'),(51,'Folkesange - Full Album','MYRKUR','Folk','Chill',2020,'Folkesange - Full Album'),(52,'Run Dancehall','Vybz Kartel','Dancehall','Energising',2021,'Run Dancehall'),(53,'MOOD ft. BNXN','WizKid','Afrobeats','Intimate',2021,'MOOD ft. BNXN'),(54,'I Need More Breakbeat in my Life!!!','MrSuicideSheep','Hardcore / Breakcore / Breakbeats','Energising',2024,'I Need More Breakbeat in my Life!!!'),(55,'Instore Session with Tomoki Tamura','Yoyaku Record Store - Live Sessions','DJ Mixes','Energising',2024,'Instore Session with Tomoki Tamura'),(56,'Live at Somerset (2019)','The Chemical Brothers','Live Performances','Energising',2019,'Live at Somerset (2019)'),(57,'The Pavillion of Dreams - Full Album','Harold Budd / Brian Eno','Alternative','Energising',1978,'The Pavillion of Dreams - Full Album'),(59,'Everything Remains Raw','Busta Rhymes','HipHop','Energising',1996,'Everything Remains Raw'),(60,'Bess, You Is My Woman Now','Miles Davis','Jazz','Chill',1958,'Bess, You Is My Woman Now'),(61,'Paradise Marsh OST','Paradise Marsh','Game OST','Chill',2023,'Paradise Marsh OST'),(62,'Sleeping Ute','Grizzly Bear','Indie','Energising',2012,'Sleeping Ute'),(63,'Baroque Choral Music - Best Works','Алик Соболевский','Classical','Chill',2020,'Baroque Choral Music - Best Works'),(64,'Forgotten | Windows 95 Retro Ambient','Retrovex Ambient','Ambient','Chill',2024,'Forgotten | Windows 85 Retro Ambient'),(65,'Plastic Love','Maria Takeuchi','Pop','Energising',1984,'Plastic Love'),(66,'BACKBONE','Chase & Status, ft. Stormzy','Drum & Bass','Energising',2024,'BACKBONE'),(67,'Soca Sex','Kerwin Du Bois','Soca','Energising',2021,'Soca Sex'),(68,'Incredible (Jungle is Massive)','General Levy','Jungle','Energising',1994,'Incredible (Jungle is Massive)'),(69,'Genisis','Justice','Electronic','Energising',2007,'Genisis'),(70,'Gremlincore Playlist','Finn','Folk','Chill',2022,'Gremlincore Playlist'),(71,'Bountie Killer vs. Beenie Man','Verzuz Presents','Dancehall','Energising',2020,'Bountie Killer vs. Beenie Man'),(72,'Premiere Gaou','Magic System','Afrobeats','Energising',2002,'Premiere Gaou'),(73,'this is a rare breakcore mix','breakcore world','Hardcore / Breakcore / Breakbeats','Energising',2024,'this is a rare breakcore mix'),(74,'Live From XOYO','Skream & Benga','DJ Mixes','Energising',2015,'Live From XOYO'),(75,'Live at the Milton Keynes Bowl, U.K. - 2010','The Prodigy - \'World\'s on Fire\' Tour','Live Performances','Energising',2010,'Live at the Milton Keynes Bowl, U.K. - 2010'),(76,'Got to Be','Childish Gambino','Alternative','Energising',2024,'Got to Be'),(83,'\'Gin and Juice\'','\'snoop dogg\'','HipHop','Gangster',1998,'https://www.youtube.com/watch?v=fWCZse1iwE0'),(94,'Chris Brown - Angel Numbers / Ten Toes (Official Video)','chris brown','Unknown','Unknown',2023,'https://www.youtube.com/watch?v=wWR0VD6qgt8');
/*!40000 ALTER TABLE `songs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-22 13:18:42
