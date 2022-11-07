import sqlite3

con = sqlite3.connect('main.sqlite3')
cur = con.cursor()
#cur.execute('CREATE TABLE EVENTS (ID INT, NAME TEXT, DESCRIPTION TEXT, YEAR INT, MONTH INT, DAY INT, HOUR INT, MINUTE INT, DONE INT);')
cur.execute(f'INSERT INTO EVENTS VALUES (0, "СДАТЬ ПРОЕКТ", "ПИПЕЦ ОСТАЛСЯ ОДИН ДЕНЬ НАМ ПИПЕЦ", 2022, 11, 8, 22, 0, 0)')
con.commit()
con.close()