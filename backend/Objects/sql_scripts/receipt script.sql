CREATE TABLE IF NOT EXISTS receipt (
receipt_id INT NOT NULL UNIQUE,
uid INT NOT NULL,
FOREIGN KEY(uid),
PRIMARY KEY(receipt_id)
);