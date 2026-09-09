import sqlite3
import pandas as pd

#CREATE TABLE 
conn=sqlite3.connect("library.db")
cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
author TEXT,
status TEXT,
price REAL
)
""")
conn.commit()
conn.close()

def add_book():
    title=input("Enter Book Title:")
    author=input("Enter Author Name:")
    status=input("Enter Status (Available/Issued):")
    price=float(input("Enter Book Price:"))

    conn=sqlite3.connect("library.db")
    cursor=conn.cursor()
    cursor.execute(
    "INSERT INTO books(title,author,price,status) VALUES(?,?,?,?)",
    (title,author,price,status))
    conn.commit()
    conn.close()
    print("Book Added Successfully.")

def delete_book():
    id=int(input("Enter Book ID:"))
    conn=sqlite3.connect("library.db")
    cursor=conn.cursor()
    cursor.execute(
    "DELETE FROM books WHERE id=?", (id))
    conn.commit()
    conn.close()
    print("Book Deleted Successfully.")

def view_books():
    conn=sqlite3.connect("library.db")
    df= pd.read_sql_query("SELECT * FROM books", conn)
    
    print(df)
    conn.close()

def search_book():
    id=int(input("Enter Book ID:"))
    conn=sqlite3.connect("library.db")
    cursor=conn.cursor()
    cursor.execute(
    "SELECT * FROM books WHERE id=?", (id))
    book=cursor.fetchone()
    conn.close()

    if book:
       print(book)
    else:
       print("Book not found.")

while True:
   print("\n==== Library Management System =====")
   print("1. Add Book")
   print("1. Update Book")
   print("1. Delete Book")
   print("1. View All Books")
   print("1. Search Book by ID")
   print("1. EXIT")

   choice=int(input("Enter choice:"))
   if choice == 1:
      add_book()
   elif choice == 2:
      delete_book()
   elif choice == 3:
      view_books()
   elif choice == 4:
        search_book()
   elif choice == 5:
       print("Thank You!")
       break
   else:
       print("Invalid Choice")

