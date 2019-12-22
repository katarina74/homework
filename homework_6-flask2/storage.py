import sqlite3
conn = sqlite3.connect("mydatabase.db")

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS articles (key integer, title text, text text, created_at text);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS comments (key integer, name text, text text);
""")

articles = [(1, "I'm so tired of everything", "Tired of everything-from work, from relationships, from the environment, from life. Just tired of everything. "
                         "\n        There is no energy, there is no drive in actions, that experienced before.\n\n        "
                         "I don't know what it is. Tried rest \u2014 did not help. What else? Quit everything? Radically, will make worse.\n\n"
                         "        Anyway, I'm tired and I don't know what to do.", "2019-12-22 06:04:49.649608"),
            (2, "dejectedly", "Once a week or two, when my father was on shift, and my mother went to the village with a car shop, took, took home, sat"
                         " at the window \n        in a kitchen garden, otkidyval obedient drum, lovingly oiled, shot, behind the chiffonier "
                         "hiding, hill, \n        the trellis creaking, parent wedding photos, and day and night Cassie sadly the clock, but "
                         "navoyevat, \n        snapping, he wrapped it in a rag again and carried it back to its place", "2019-12-22 06:01:02.241511")]

comments = [(1, "Ivan Ivanov", "relevant"), (1, "Katya Ivanova", ")))"),(2, "thesweetguard", "nice")]

cursor.executemany("INSERT INTO articles (key, title, text, created_at) values (?, ?, ?, ?)", articles)

cursor.executemany("INSERT INTO comments (key, name, text) values (?, ?, ?)", comments)

conn.commit()
