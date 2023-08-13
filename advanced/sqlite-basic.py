import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (username, password)")
connection.commit()
print("Database created")

cursor.execute("INSERT INTO users VALUES ('admin','123456')")
connection.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

cursor.execute("SELECT * FROM users WHERE username='admin'")

connection.close()
