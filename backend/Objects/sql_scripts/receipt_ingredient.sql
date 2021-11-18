CREATE TABLE IF NOT EXISTS receipt_ingredient (
receipt_id INT NOT NULL,
fid INT NOT NULL,
weight float NOT NULL,
date DATETIME NOT NULL,
FOREIGN KEY(receipt_id) REFERENCES receipt(receipt_id),
FOREIGN KEY(fid) REFERENCES food_item(fid),
PRIMARY KEY(receipt_id,fid)
);