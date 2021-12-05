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

INSERT INTO `recipe` VALUES 
(1,'Singapore Chicken Wings','chickenwing:2000',118,'Chinese Food','5 tbsp oyster sauce, 1.5 tbsp dark soya sauce, 2 tbsp light soya sauce, 1.5 tbsp honey, 4 tbsp sesame oil, 3 tbsp salt','http://mysingaporefood.com/recipe/singapores-best-chicken-wings/'),
(2,'Green Chilli Prawn Sambal','prawns: 1000',192,'Malay Food','15 pcs long green chillies, sliced ½ – ¾ cup thick coconut milk (from 200g grated fresh coconut), 1 tsp sugar, 2 tsp salt or to taste, ¾ cup oil, REMPAH/PASTE: 350g shallots 5 or 6 pcs green chilli padi, 12 pcs candlenuts, 3cm turmeric, 2cm square piece of belachan/shrimp paste, 6 cloves garlic, 2 stalks lemongrass cut into 2cm pieces and lightly bashed','http://mysingaporefood.com/?s=green+chilli'),
(3,'Fish Masala','fish:1000',306,'Indian Food','MASALA PASTE BLEND: 1 grated coconut (500g), 3 tbs black peppercorns, 1 ½ tbs cumin seeds, 3 tbs fennel seeds, 4 ½ tbs chilli powder, ½ tsp turmeric powder, 2 cloves garlic, 1-inch ginger, 2 ½ tsp salt or to taste, 3 cups water','http://mysingaporefood.com/recipe/fish-masala/'),
(4,'Udang Goreng Assam','prawns:500',197,'Malay Food','MARINADE 1 tbsp assam paste, 1 tbsp thick dark soya sauce, 2 tbsp sugar','http://mysingaporefood.com/recipe/udang-goreng-assam/'),
(5,'Steamed Pork In Prawn Paste','streaky pork:200',227,'Chinese Food','2 tsp prawn paste, 1 tsp sugar, ½ tsp corn starch, 1 slice tangerine peel, 1 pc red chilli sliced (for garnish), spring onions sliced (for garnish), a pinch of pepper, cooking oil','http://mysingaporefood.com/recipe/steamed-pork-in-prawn-paste/'),
(6,'Fried Chicken Wings with Kicap Manis','chickenwing:4000',400,'Malay Food','tamarind pulp – ½ cup, fish sauce – 1 tea spoon, SPICE BLEND: cumin powder – 1 tea spoon, tumeric powder – 1 tea spoon, chilli powder – 1 tea spoon, salt – 1 tea spoon, fish curry powder – 1 tea spoon, oil for frying, KECAP MANIS DIP kecap manis – ½ cup, chopped chili padi – 1 whole, sliced shallots – 3 whole, calamansi juice – 3, 4 whole chopped coriander leaves','http://mysingaporefood.com/recipe/fried-chicken-wings-with-kicap-manis/'),
(7,'Granny’s Chicken Soup','chicken:3000',204,'Chinese Food','1 large thumb young ginger thinly sliced, 3 stalks spring onions sliced about an inch long, 1 tsp top-grade sesame oil, 1 tsp canola oil, 6 cloves garlic lightly bashed with skin removed, 1/2 tsp coriander seeds bashed in mortar and pestle, 1 tsp white peppercorns bashed in mortar and pestle, 2 large dried scallops pre-soaked in cold water for 10-15 minutes, 2 litres water, 2 tins mushrooms drained, 3 large strips fish maw (Prepare with hot and not boiling water. Soak in the hot water for 30 minutes and rinse under cold water before cutting into strips), a pinch of salt to taste, coriander leaves for garnish','http://mysingaporefood.com/recipe/grannys-chicken-soup/');