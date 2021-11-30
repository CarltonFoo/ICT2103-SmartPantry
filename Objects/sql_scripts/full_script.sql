CREATE database IF NOT EXISTS smartpantry;

USE smartpantry;

CREATE TABLE IF NOT EXISTS food_item (
  fid INT NOT NULL UNIQUE,
  food_name VARCHAR(255) NOT NULL,
  price FLOAT NOT NULL,
  weight FLOAT NOT NULL,
  primary key(fid)
);

CREATE TABLE IF NOT EXISTS recipe (
  rid INT UNIQUE NOT NULL,
  recipe_name VARCHAR(255) NOT NULL,
  main_ingredients VARCHAR(255) NOT NULL,
  calories INT NOT NULL,
  dietary_type VARCHAR(255) NOT NULL,
  marinates LONGTEXT,
  steps VARCHAR(255),
  primary key(rid)
);

CREATE TABLE IF NOT EXISTS user(
  id INT AUTO_INCREMENT UNIQUE,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  gender CHAR(1) NOT NULL,
  age INT NOT NULL,
  height FLOAT NOT NULL,
  weight FLOAT,
  profile_bio VARCHAR(255),
  dietary_needs VARCHAR(255),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS receipt (
  receipt_id INT AUTO_INCREMENT NOT NULL UNIQUE,
  id INT NOT NULL,
  total_amount FLOAT NOT NULL,
  FOREIGN KEY(id) REFERENCES user(id),
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
  id INT NOT NULL,
  fid INT NOT NULL,
  weight float NOT NULL,
  FOREIGN KEY(id) REFERENCES user(id),
  FOREIGN KEY(fid) REFERENCES food_item(fid),
  PRIMARY KEY(id, fid)
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
  id INT NOT NULL,
  date DATETIME NOT NULL,
  type VARCHAR(255) NOT NULL references recipe(type),
  FOREIGN KEY(rid) REFERENCES recipe(rid),
  FOREIGN KEY(id) REFERENCES user(id),
  PRIMARY KEY(rid, id)
);



-- User
INSERT INTO `user` VALUES 
(1,'johanna','6e1e4c2ac39461e8362b2409fb7870811f65b8f4ad82fb42fb15c976f76a785991f2c0ef6c8babb1c0761318deb7f6b324bfcf8d3ef1651c1661e76d19e889b6','F',22,159,62,'',''),
(2,'bianca','aa60b14056e06b7c2041990f836e634fab14c251a11fdec41799f788be7c74d8ebcafa14a2171c82575fcbde68fdca45f1bab406160cfd61e52750f63263f056','F',24,0,0,'',''),
(3,'carlton','bb8cd751db281025451d01f4e847aeac30622c33888a096e54bce11dfbd5a5a79a51de73c04126e84eba3d2bd78af7cf5ca9fbae4b29336412f814a12c95df12','M',23,123,123,'diet','bio');


-- Food Item
INSERT INTO `food_item` VALUES 
(1,'Premium Thai Rice',13.75,5000),
(2,'Ordinary White Bread',1.74,400),
(3,'Vitamin Enriched Bread',1.63,400),
(4,'Wholemeal Bread',2.1,400),
(5,'Lean Pork (Chilled)',15.32,1000),
(6,'Streaky Pork (Chilled)',17.19,1000),
(7,'Pork Rib Bones (Chilled)',18.51,1000),
(8,'Beef (Chilled)',25.18,1000),
(9,'Mutton (Chilled)',22.03,1000),
(10,'Whole Chicken (Chilled)',6.32,1000),
(11,'Chicken Wing (Chilled)',8.43,1000),
(12,'Duck, Chilled',7.17,1000),
(13,'Lean Pork (Frozen)',4.9,500),
(14,'Pork Rib Bones (Frozen)',5.88,500),
(15,'Cod Fish',65.63,1000),
(16,'Gold Banded Scad (Kuning)',8.21,1000),
(17,'Flowery Grouper',13.75,1000),
(18,'White Pomfret',30.15,1000),
(19,'Salmon',29.83,1000),
(20,'Sea Bass',11.7,1000),
(21,'Sea Bream (Ang Ko Li)',9.93,1000),
(22,'Golden Snapper',18.79,1000),
(23,'Spanish Mackerel (Batang)',12.95,1000),
(24,'Threadfin (Kurau)',60.32,1000),
(25,'Small Prawns',15.28,1000),
(26,'Medium Prawns',20.12,1000),
(27,'Squids',17.72,1000),
(28,'Infant Milk Powder',6.16,100),
(29,'Cooking Oil',6.21,2000),
(30,'Bananas',2.43,1000),
(31,'Papaya',2.2,1000),
(32,'Watermelon',1.59,1000),
(33,'Grapes',11.18,1000),
(34,'Orange',0.59,0),
(35,'Apple',0.43,0),
(36,'Pear',1.28,0),
(37,'Broccoli',5.7,1000),
(38,'Cabbage',2.34,1000),
(39,'Chinese Kale (Kailan)',5.19,1000),
(40,'Small Mustard (Chye Sim)',3.98,1000),
(41,'Spinach (Bayam)',3.57,1000),
(42,'Tomatoes',2.63,1000),
(43,'Potatoes',2.41,1000),
(44,'Carrots',2.03,1000),
(45,'White Sugar',3.08,2000),
(46,'Instant Coffee',10.19,200);


-- Recipe
INSERT INTO `recipe` VALUES 
(1,'Singapore Chicken Wings','chickenwing:2000',118,'Chinese Food','5 tbsp oyster sauce, 1.5 tbsp dark soya sauce, 2 tbsp light soya sauce, 1.5 tbsp honey, 4 tbsp sesame oil, 3 tbsp salt','http://mysingaporefood.com/recipe/singapores-best-chicken-wings/'),
(2,'Green Chilli Prawn Sambal','prawns: 1000',192,'Malay Food','15 pcs long green chillies, sliced ½ – ¾ cup thick coconut milk (from 200g grated fresh coconut), 1 tsp sugar, 2 tsp salt or to taste, ¾ cup oil, REMPAH/PASTE: 350g shallots 5 or 6 pcs green chilli padi, 12 pcs candlenuts, 3cm turmeric, 2cm square piece of belachan/shrimp paste, 6 cloves garlic, 2 stalks lemongrass cut into 2cm pieces and lightly bashed','http://mysingaporefood.com/?s=green+chilli'),
(3,'Fish Masala','fish:1000',306,'Indian Food','MASALA PASTE BLEND: 1 grated coconut (500g), 3 tbs black peppercorns, 1 ½ tbs cumin seeds, 3 tbs fennel seeds, 4 ½ tbs chilli powder, ½ tsp turmeric powder, 2 cloves garlic, 1-inch ginger, 2 ½ tsp salt or to taste, 3 cups water','http://mysingaporefood.com/recipe/fish-masala/'),
(4,'Udang Goreng Assam','prawns:500',197,'Malay Food','MARINADE 1 tbsp assam paste, 1 tbsp thick dark soya sauce, 2 tbsp sugar','http://mysingaporefood.com/recipe/udang-goreng-assam/'),
(5,'Steamed Pork In Prawn Paste','streaky pork:200',227,'Chinese Food','2 tsp prawn paste, 1 tsp sugar, ½ tsp corn starch, 1 slice tangerine peel, 1 pc red chilli sliced (for garnish), spring onions sliced (for garnish), a pinch of pepper, cooking oil','http://mysingaporefood.com/recipe/steamed-pork-in-prawn-paste/'),
(6,'Fried Chicken Wings with Kicap Manis','chickenwing:4000',400,'Malay Food','tamarind pulp – ½ cup, fish sauce – 1 tea spoon, SPICE BLEND: cumin powder – 1 tea spoon, tumeric powder – 1 tea spoon, chilli powder – 1 tea spoon, salt – 1 tea spoon, fish curry powder – 1 tea spoon, oil for frying, KECAP MANIS DIP kecap manis – ½ cup, chopped chili padi – 1 whole, sliced shallots – 3 whole, calamansi juice – 3, 4 whole chopped coriander leaves','http://mysingaporefood.com/recipe/fried-chicken-wings-with-kicap-manis/'),
(7,'Granny’s Chicken Soup','chicken:3000',204,'Chinese Food','1 large thumb young ginger thinly sliced, 3 stalks spring onions sliced about an inch long, 1 tsp top-grade sesame oil, 1 tsp canola oil, 6 cloves garlic lightly bashed with skin removed, 1/2 tsp coriander seeds bashed in mortar and pestle, 1 tsp white peppercorns bashed in mortar and pestle, 2 large dried scallops pre-soaked in cold water for 10-15 minutes, 2 litres water, 2 tins mushrooms drained, 3 large strips fish maw (Prepare with hot and not boiling water. Soak in the hot water for 30 minutes and rinse under cold water before cutting into strips), a pinch of salt to taste, coriander leaves for garnish','http://mysingaporefood.com/recipe/grannys-chicken-soup/');


-- Receipt
INSERT INTO `receipt` VALUES 
(1,1,22.12),
(2,1,16.86);


-- Receipt Ingredient
INSERT INTO `receipt_ingredient` VALUES 
(1,1,5000,'2021-11-30'),
(1,2,800,'2021-11-30'),
(1,3,1200,'2021-11-30'),
(2,11,2000,'2021-11-30');

