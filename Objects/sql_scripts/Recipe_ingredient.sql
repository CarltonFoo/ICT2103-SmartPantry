CREATE TABLE IF NOT EXISTS recipe_ingredient(
rid INT NOT NULL,
fid INT NOT NULL,
weight float NOT NULL,
FOREIGN KEY(rid) REFERENCES recipe(rid),
FOREIGN KEY(fid) REFERENCES food_item(fid),
PRIMARY KEY(rid,fid)
);