CREATE TABLE IF NOT EXISTS receipt_ingredient (
  receipt_id INT NOT NULL,
  fid INT NOT NULL,
  weight float NOT NULL,
  date DATETIME NOT NULL,
  FOREIGN KEY(receipt_id) REFERENCES receipt(receipt_id),
  FOREIGN KEY(fid) REFERENCES food_item(fid),
  PRIMARY KEY(receipt_id, fid)
);

INSERT INTO `receipt_ingredient` VALUES 
(1,1,5000,'2021-11-30'),
(1,2,800,'2021-11-30'),
(1,3,1200,'2021-11-30'),
(2,11,2000,'2021-11-30');