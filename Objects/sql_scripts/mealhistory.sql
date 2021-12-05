CREATE TABLE IF NOT EXISTS mealhistory (
  rid INT NOT NULL,
  id INT NOT NULL,
  date DATETIME NOT NULL,
  FOREIGN KEY(rid) REFERENCES recipe(rid),
  FOREIGN KEY(id) REFERENCES user(id),
  PRIMARY KEY(rid, id)
);


INSERT INTO `receipt_ingredient` VALUES 
(3,1,'2021-12-01'),
(1,1,'2021-11-02'),
(2,2,'2021-11-03'),
(5,2,'2021-11-03'),
(7,3,'2021-11-03'),
(6,3,'2021-11-03'),
(4,4,'2021-11-04');