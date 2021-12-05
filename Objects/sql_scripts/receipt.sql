CREATE TABLE IF NOT EXISTS receipt (
receipt_id INT NOT NULL UNIQUE,
id INT NOT NULL,
total_amount FLOAT NOT NULL,
FOREIGN KEY(id) REFERENCES user(id),
PRIMARY KEY(receipt_id)
);


-- Receipt
INSERT INTO `receipt` VALUES 
(1,1,22.12),
(2,1,16.86);