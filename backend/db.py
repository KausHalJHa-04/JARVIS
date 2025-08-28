# import csv
import csv
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

query = "INSERT INTO web_command VALUES(null,'whatapp web', 'https://web.whatsapp.com/')"
cursor.execute(query)
conn.commit()

# query = "DELETE FROM contact WHERE name='Phone'"
# cursor.execute(query)
# conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name VARCHAR(200), Phone VARCHAR(255), email VARCHAR(255) NULL)''') 


# desired_columns_indices = [0, 1]
 
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'Phone') VALUES (null, ?,? );''', tuple(selected_data))

# # Commit changes and close connection
# conn.commit()
# conn.close()
# print("Data inserted successfully") 

query = "INSERT INTO contacts VALUES (null,'kishore', '8882445461', 'null')"
cursor.execute(query)
conn.commit() 



# query = 'kishor'
# query = query.strip().lower()  # Added parentheses to call the method

# cursor.execute("SELECT Phone FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", 
#                ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])