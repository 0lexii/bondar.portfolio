import sqlite3

conn = sqlite3.connect('dictionary.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS vocab
        (id INTEGER PRIMARY KEY,
        food BOOL,
        color BOOL,
        clothes BOOL,
        transport BOOL,
        jobs BOOL,
        german TEXT COLLATE NOCASE,
        ukrainian TEXT)''')

c.execute('''INSERT INTO vocab VALUES
        (1, TRUE, FALSE, FALSE, FALSE, FALSE, 'Hühnerchen', 'курка'),
        (2, FALSE, TRUE, FALSE, FALSE, FALSE, 'Schwarz', 'чорний'),
        (3, FALSE, FALSE, TRUE, FALSE, FALSE, 'Bluse', 'блузка'),
        (4, FALSE, FALSE, FALSE, TRUE, FALSE, 'Auto', 'автомобіль'),
        (5, FALSE, FALSE, FALSE, FALSE, TRUE, 'Arzt', 'лікар'),
        (6, TRUE, FALSE, FALSE, FALSE, FALSE, 'Rindfleisch', 'яловичина'),
        (7, FALSE, TRUE, FALSE, FALSE, FALSE, 'Weiß', 'білий'),
        (8, FALSE, FALSE, TRUE, FALSE, FALSE, 'Kleid', 'сукня'),
        (9, FALSE, FALSE, FALSE, TRUE, FALSE, 'Bus', 'автобус'),
        (10, FALSE, FALSE, FALSE, FALSE, TRUE, 'Buchhalter', 'бухгалтер'),
        (11, TRUE, FALSE, FALSE, FALSE, FALSE, 'Fisch', 'риба'),
        (12, FALSE, TRUE, FALSE, FALSE, FALSE, 'Grau', 'сірий'),
        (13, FALSE, FALSE, TRUE, FALSE, FALSE, 'Rock', 'спідниця'),
        (14, FALSE, FALSE, FALSE, TRUE, FALSE, 'Fahrrad', 'велосипед'),
        (15, FALSE, FALSE, FALSE, FALSE, TRUE, 'Ingenieur', 'інженер'),
        (16, TRUE, FALSE, FALSE, FALSE, FALSE, 'Schweinefleisch', 'свинина'),
        (17, FALSE, TRUE, FALSE, FALSE, FALSE, 'Rot', 'червоний'),
        (18, FALSE, FALSE, TRUE, FALSE, FALSE, 'T-Shirt', 'футболка'),
        (19, FALSE, FALSE, FALSE, TRUE, FALSE, 'Motorrad', 'мотоцикл'),
        (20, FALSE, FALSE, FALSE, FALSE, TRUE, 'Taxifahrer', 'таксист'),
        (21, TRUE, FALSE, FALSE, FALSE, FALSE, 'Wurst', 'ковбаса'),
        (22, FALSE, TRUE, FALSE, FALSE, FALSE, 'Blau', 'синій'),
        (23, FALSE, FALSE, TRUE, FALSE, FALSE, 'Hemd', 'сорочка'),
        (24, FALSE, FALSE, FALSE, TRUE, FALSE, 'U-Bahn', 'метро'),
        (25, FALSE, FALSE, FALSE, FALSE, TRUE, 'Dolmetscher', 'перекладач'),
        (26, TRUE, FALSE, FALSE, FALSE, FALSE, 'Käse', 'сир'),
        (27, FALSE, TRUE, FALSE, FALSE, FALSE, 'Gelb', 'жовтий'),
        (28, FALSE, FALSE, TRUE, FALSE, FALSE, 'Hose', 'штани'),
        (29, FALSE, FALSE, FALSE, TRUE, FALSE, 'Straßenbahn', 'трамвай'),
        (30, FALSE, FALSE, FALSE, FALSE, TRUE, 'Krankenschwester', 'медсестра'), 
        (31, TRUE, FALSE, FALSE, FALSE, FALSE, 'Gemüse', 'овочі'),
        (32, FALSE, TRUE, FALSE, FALSE, FALSE, 'Grün', 'зелений'),
        (33, FALSE, FALSE, TRUE, FALSE, FALSE, 'Gürtel', 'ремінь'),
        (34, FALSE, FALSE, FALSE, TRUE, FALSE, 'Zug', 'потяг'),
        (35, FALSE, FALSE, FALSE, FALSE, TRUE, 'Bauarbeiter', 'будівельник'),
        (36, TRUE, FALSE, FALSE, FALSE, FALSE, 'Obst', 'фрукти'),
        (37, FALSE, TRUE, FALSE, FALSE, FALSE, 'Orange', 'помаранчевий'),
        (38, FALSE, FALSE, TRUE, FALSE, FALSE, 'Pullover', 'светр'),
        (39, FALSE, FALSE, FALSE, TRUE, FALSE, 'Flugzeug', 'літак'),
        (40, FALSE, FALSE, FALSE, FALSE, TRUE, 'Tierarzt', 'ветеринар'), 
        (41, TRUE, FALSE, FALSE, FALSE, FALSE, 'Nudeln', 'локшина'),
        (42, FALSE, TRUE, FALSE, FALSE, FALSE, 'Violett', 'фіолетовий'),
        (43, FALSE, FALSE, TRUE, FALSE, FALSE, 'Jacke', 'піджак'),
        (44, FALSE, FALSE, FALSE, TRUE, FALSE, 'Boot', 'човен'),
        (45, FALSE, FALSE, FALSE, FALSE, TRUE, 'Verkäufer', 'продавець'), 
        (46, TRUE, FALSE, FALSE, FALSE, FALSE, 'Reis', 'рис'),
        (47, FALSE, TRUE, FALSE, FALSE, FALSE, 'Braun', 'коричневий'),
        (48, FALSE, FALSE, TRUE, FALSE, FALSE, 'Mantel', 'пальто'),
        (49, FALSE, FALSE, FALSE, TRUE, FALSE, 'Schiff', 'корабель'),
        (50, FALSE, FALSE, FALSE, FALSE, TRUE, 'Koch', 'кухар')''')

conn.commit()
conn.close()
