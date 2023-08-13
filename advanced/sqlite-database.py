import sqlite3 as sql

# Connect to the database
connection = sql.connect("database.db")
cursor = connection.cursor()

# Drop the table if it exists
cursor.execute("DROP TABLE IF EXISTS users")

# Create the table
cursor.execute("CREATE TABLE IF NOT EXISTS users (username, password)")
print("Database created")

# Commit the changes
connection.commit()

# Insert records into the table
cursor.execute("INSERT INTO users VALUES ('admin', '1234566')")
cursor.execute("INSERT INTO users VALUES ('berkay', '1234566')")
connection.commit()

# Fetch and display records from the table
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# Close the database connection
connection.close()
