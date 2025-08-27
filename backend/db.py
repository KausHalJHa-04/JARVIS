# import csv
import sqlite3

conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)
query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO sys_command VALUES(null,'sticky note', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')"
# cursor.execute(query)
# conn.commit()

# query = "INSERT INTO web_command VALUES(null,'Git Hub', 'https://github.com/')"
# cursor.execute(query)
# conn.commit()

# query = "INSERT INTO web_command VALUES(null,'whatapp web', 'https://web.whatsapp.com/')"
# cursor.execute(query)
# conn.commit()

query = "DELETE FROM sys_command WHERE name='whatapp web'"
cursor.execute(query)
conn.commit()