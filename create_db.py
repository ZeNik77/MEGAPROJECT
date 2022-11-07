import sqlite3

con = sqlite3.connect('Assets/Databases/main.sqlite3')
cur = con.cursor()
cur.execute('CREATE TABLE EVENTS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT DEFAULT "Название", DESCRIPTION TEXT DEFAULT "Описание", YEAR INT, MONTH INT, DAY INT, HOUR INT DEFAULT 0, MINUTE INT DEFAULT 0, DONE INT DEFAULT 0);')
cur.execute(f'INSERT INTO EVENTS VALUES (0, "СДАТЬ ПРОЕКТ", "ПИПЕЦ ОСТАЛСЯ ОДИН ДЕНЬ НАМ ПИПЕЦ", 2022, 11, 8, 22, 0, 0)')
cur.execute('CREATE TABLE TASKS (ID INTEGER PRIMARY KEY AUTOINCREMENT, CONTENT TEXT DEFAULT "", COLUMN INT DEFAULT 1)')
con.commit()
con.close()