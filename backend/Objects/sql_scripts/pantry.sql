CREATE TABLE IF NOT EXISTS pantry(
uid INT NOT NULL,
fid INT NOT NULL,
weight float NOT NULL,
FOREIGN KEY(uid) REFERENCES user(uid),
FOREIGN KEY(fid) REFERENCES food_item(fid),
PRIMARY KEY(uid,fid)
);