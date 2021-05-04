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
'''c= conn.cursor()

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
'''
def submit():
    # Create a database or connect to connect one
    conn=sqlite3.connect("Address_book.db")

    # create cursor
    c=conn.cursor()

    #insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",{
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get(),
        'zipcode':zipcode.get(),

    })
    print("address inserted successfully")

    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    city.delete(0,END)
    zipcode.delete(0,END)


f_name=Entry(root, width=30)
f_name.grid(row=1, column=1)
f_name_label=Label(root, text="First name")
f_name_label.grid(row=1, column=0)

l_name=Entry(root, width=30)
l_name.grid(row=2, column=1)
l_name_label=Label(root, text="Last name")
l_name_label.grid(row=2, column=0)

address=Entry(root, width=30)
address.grid(row=3, column=1)
address_label=Label(root, text="address")
address_label.grid(row=3, column=0)

city=Entry(root, width=30)
city.grid(row=4, column=1)
city_label=Label(root, text="city")
city_label.grid(row=4, column=0)

state=Entry(root, width=30)
state.grid(row=5, column=1)
state_label=Label(root, text="State")
state_label.grid(row=5, column=0)

zipcode=Entry(root, width=30)
zipcode.grid(row=6, column=1)
zipcode_label=Label(root, text="Zipcode")
zipcode_label.grid(row=6, column=0)


submit_button=Button(root, text="Add Records", command=submit)
submit_button.grid(row=7, column=0, columnspan=2, pady=30)

# commit change
conn.commit()

# close connection
conn.close()

mainloop()