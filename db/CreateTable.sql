CREATE TABLE exoplanet (
    id         INTEGER NOT NULL AUTO_INCREMENT,
    name       VARCHAR(30) NOT NULL,
    system     VARCHAR(30) NOT NULL,
    method     VARCHAR(150) NOT NULL,
    year       INTEGER NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `exoplanet` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO 'exoplanet'
VALUES 
    (1,'Earth','Solar','Looking', 1972),
    (2,'Kepler 16b','Kepler','Transit', 2016),
    (3,'Test','system','method', 55);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;