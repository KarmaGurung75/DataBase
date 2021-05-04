from tkinter import *
import sqlite3
root= Tk()
root.title("Database Address Book")

# Database

# create a database or connect to one
conn=sqlite3.connect("address_book.db")

# create cursor
# cursor  class is an instance using which you can invoke methods that
# execute SQLite statement, fetch data from the result sets of the quries
c= conn.cursor()

# create table
c.execute("""CREATE TABLE addresses(
         first_name text,
         last_name text,
         address text,
         city text,
         state text,
         zipcode integer
)
""")
print("Table Create successfully")

# commit change
conn.commit()

# close connection
conn.close()

mainloop()