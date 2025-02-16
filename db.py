import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(100))"
cursor.execute(query)

#query = "INSERT INTO sys_command VALUES (null,'vs code','D:\\Microsoft VS Code\\Code.exe')"
#cursor.execute(query)
#con.commit()

#query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(100))"
#cursor.execute(query)

#query = "INSERT INTO web_command VALUES (null,'youtube','https://www.youtube.com/')"
#cursor.execute(query)
#con.commit()
# query = "INSERT INTO web_command VALUES (null,'wikipedia','https://en.wikipedia.org/wiki/Main_Page')"
# cursor.execute(query)
# con.commit()
query = "INSERT INTO web_command VALUES (null,'youtube','https://www.facebook.com/')"
cursor.execute(query)
con.commit()