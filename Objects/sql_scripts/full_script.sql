CREATE database IF NOT EXISTS smartpantry;

USE smartpantry;

CREATE TABLE IF NOT EXISTS food_item (
  fid INT NOT NULL UNIQUE,
  food_name VARCHAR(255) NOT NULL,
  price FLOAT NOT NULL,
  weight FLOAT NOT NULL,
  calories INT,
  primary key(fid)
);

CREATE TABLE IF NOT EXISTS recipe (
  rid INT UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  type VARCHAR(255) NOT NULL,
  calories INT NOT NULL,
  description VARCHAR(255),
  dietary_needs VARCHAR(255),
  primary key(rid)
);

CREATE TABLE IF NOT EXISTS user(
  uid INT AUTO_INCREMENT UNIQUE,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  gender CHAR(1) NOT NULL,
  height FLOAT NOT NULL,
  weight FLOAT,
  profile_bio VARCHAR(255),
  dietary_needs VARCHAR(255),
  age INT NOT NULL,
  PRIMARY KEY (uid)
);

CREATE TABLE IF NOT EXISTS receipt (
  receipt_id INT AUTO_INCREMENT NOT NULL UNIQUE,
  uid INT NOT NULL,
  FOREIGN KEY(uid) REFERENCES user(uid),
  PRIMARY KEY(receipt_id)
);

CREATE TABLE IF NOT EXISTS receipt_ingredient (
  receipt_id INT NOT NULL,
  fid INT NOT NULL,
  weight float NOT NULL,
  date DATETIME NOT NULL,
  FOREIGN KEY(receipt_id) REFERENCES receipt(receipt_id),
  FOREIGN KEY(fid) REFERENCES food_item(fid),
  PRIMARY KEY(receipt_id, fid)
);

CREATE TABLE IF NOT EXISTS pantry(
  uid INT NOT NULL,
  fid INT NOT NULL,
  weight float NOT NULL,
  FOREIGN KEY(uid) REFERENCES user(uid),
  FOREIGN KEY(fid) REFERENCES food_item(fid),
  PRIMARY KEY(uid, fid)
);

CREATE TABLE IF NOT EXISTS recipe_ingredient(
  rid INT NOT NULL,
  fid INT NOT NULL,
  weight float NOT NULL,
  FOREIGN KEY(rid) REFERENCES recipe(rid),
  FOREIGN KEY(fid) REFERENCES food_item(fid),
  PRIMARY KEY(rid, fid)
);

CREATE TABLE IF NOT EXISTS MealHistory (
  rid INT NOT NULL,
  uid INT NOT NULL,
  date DATETIME NOT NULL,
  type VARCHAR(255) NOT NULL references recipe(type),
  FOREIGN KEY(rid) REFERENCES recipe(rid),
  FOREIGN KEY(uid) REFERENCES user(uid),
  PRIMARY KEY(rid, uid)
);