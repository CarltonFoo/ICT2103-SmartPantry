CREATE TABLE IF NOT EXISTS user(
id INT AUTO_INCREMENT UNIQUE, 
username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  gender CHAR(1) NOT NULL,
  height FLOAT NOT NULL,
  weight FLOAT, 
  profile_bio VARCHAR(255),
  dietary_needs VARCHAR(255),
  age INT NOT NULL,
  PRIMARY KEY (id)
  );