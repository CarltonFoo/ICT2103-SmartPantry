CREATE TABLE IF NOT EXISTS Recipe ( rid INT UNIQUE NOT NULL,
 name VARCHAR(255) NOT NULL,
 type VARCHAR(255) NOT NULL,
 calories INT NOT NULL,
 description VARCHAR(255),
 dietary_needs VARCHAR(255),
 primary key(rid)
 );