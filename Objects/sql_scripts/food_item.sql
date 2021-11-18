CREATE TABLE IF NOT EXISTS food_item (fid INT NOT NULL UNIQUE,
food_name VARCHAR(255) NOT NULL,
price FLOAT NOT NULL,
weight FLOAT NOT NULL,
calories INT,
 primary key(fid)
 );