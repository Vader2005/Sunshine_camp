from tkinter import *
import sqlite3

main_window = Tk()

# Making the database

# Create the database table
conn = sqlite3.connect('Info_people.db')

# Create the cursor
c = conn.cursor()

# Create the table
c.execute("""CREATE TABLE info (
        Leader text,
        Location text,
        Weather text,
        Row integer,
        Number_campers integer)
""")

# Commit changes to databse
conn.commit()

# Close connection
conn.close()

main_window.geometry("500x500")
main_window.mainloop()

# Base code
# Run this once
