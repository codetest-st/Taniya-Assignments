import sqlite3
conn=sqlite3.connect("college.db")
print("Database created and opened successfully")
conn.close()