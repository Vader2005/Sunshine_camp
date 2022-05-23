from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

main_window = Tk()

# Making the database

# Create the database table
conn = sqlite3.connect('Info_people.db')

# Create the cursor
c = conn.cursor()

# Create the table
'''
c.execute("""CREATE TABLE info (
        Leader text,
        Location text,
        Weather text,
        Row integer,
        Number_campers integer)
""")
'''

# Create function to delete a row

def check_inputs():
    input_check = 0

    # Make sure Leader entry is not empty
    if len(Leader_entry.get()) == 0:
        messagebox.showerror("showerror", "Error, Leader entry cannot be empty")
        input_check = 1

    # Check that the location is not blank
    if len(Location_entry.get()) == 0:
        messagebox.showerror("showerror", "Error, Location entry cannot be empty")
        input_check = 1

    # Check that the weather cannot be empty
    if len(weather.get()) == 0:
        messagebox.showerror("showerror", "Error, Weather cannot be blank")
        input_check = 1

    # Check that row cannot be empty
    if len(Row_entry.get()) == 0:
        messagebox.showerror("showerror", "Error, Row cannot be blank")
        input_check = 1

    # Run the submit function if all entries are validated
    if input_check == 0:
        submit()


def delete():
    # Connect to the database
    conn = sqlite3.connect('Info_people.db')
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE FROM info WHERE oid=" + delete_entry.get())

    # Close database
    conn.commit()
    conn.close()

# Building submit button function

def submit():
        # Create the cursor and connect it to the function
        conn = sqlite3.connect('Info_people.db')
        c = conn.cursor()

        # Insert values into the database
        c.execute("INSERT INTO info VALUES (:Leader_entry, :Location_entry, :Row_entry, :campers, :weather)",
                {
                        'Leader_entry': Leader_entry.get(),
                        'Location_entry': Location_entry.get(),
                        'Row_entry': Row_entry.get(),
                        'campers': campers.get(),
                        'weather': weather.get()
                }
        
        )

        # Close the database
        conn.commit()
        conn.close()

        # Clear the entries and spin/combo boxes
        Leader_entry.delete(0, 'end')
        Location_entry.delete(0, 'end')
        Row_entry.delete(0, 'end')
        campers.set('')
        weather.set('')

# Building query button function

def query():
        # Create the cursor and connect it to the function
        conn = sqlite3.connect('Info_people.db')
        c = conn.cursor()

        # Query the database
        c.execute("SELECT *, oid FROM info")
        records = c.fetchall()
        #print(records)

        # Loop through the database and print results
        print_record = ''

        for record in records:
                print_record += str(record[0]) + "\t\t" + str(record[1]) + "\t\t" + str(record[2]) + "\t\t" + str(record[3]) + "\t\t" + str(record[4]) + "\t\t" + str(record[5]) + '\n'

        display_label = Label(main_window, text=print_record).place(x=50, y=250)

        # Create heading labels
        Leader_display_label = Label(main_window, text="Leader").place(x=50, y=200)
        Location_display_label = Label(main_window, text="Location").place(x=145, y=200)
        Row_display_label = Label(main_window, text="Row").place(x=235, y=200)
        Number_display_label = Label(main_window, text="Num of campers").place(x=300, y=200)
        Weather_display_label = Label(main_window, text="Weather").place(x=430, y=200)
        oid_display_number = Label(main_window, text="Oid").place(x=525, y=200)

        # Close the database
        conn.commit()
        conn.close()

# Building the GUI

# Building the Labels

Leader_label = Label(main_window, text="Leader: ").place(x=10, y=70)
Location_label = Label(main_window, text="Location: ").place(x=10, y=90)
Number_label = Label(main_window, text="Number of campers: ").place(x=10, y=110)
Weather_label = Label(main_window, text="Weather: ").place(x=10, y=130)
Row_label = Label(main_window, text="Row: ").place(x=10, y=150)
delete_label = Label(main_window, text="Enter oid to delete: ").place(x=375, y=80)

# Building the Entries

Leader_entry = Entry(main_window)
Leader_entry.place(x=150, y=70)
Location_entry = Entry(main_window)
Location_entry.place(x=150, y=90)
Row_entry = Entry(main_window)
Row_entry.place(x=150, y=150)
delete_entry = Entry(main_window)
delete_entry.place(x=500, y=80)

# Creating the quit button
quit_button = Button(main_window, text="Quit", command=exit).place(x=130, y=5)

# Spinbox for the numbers of campers
campers = StringVar()
num_campers = Spinbox(main_window, from_=5, to=10, textvariable=campers, wrap=False, state='readonly').place(x=150, y=110)

# Creating the combobox for weather
weather = StringVar()
weathers = ['Sunny', 'Cloudy', 'Rainy', 'storm', 'Hail']
weather_entry = ttk.Combobox(main_window, textvariable=weather, state='readonly', value=weathers).place(x=150, y=130)

# Creating the submit info button
submit_button = Button(main_window, text="Submit info", command=check_inputs).place(x=10, y=35)

# Creating querying info button
query_button = Button(main_window, text="Print info", command=query).place(x=130, y=35)

# Create a delete button
delete_button = Button(main_window, text="Delete info", command=delete).place(x=450, y=130)

# Commit changes to databse
conn.commit()

# Close connection
conn.close()

main_window.geometry("700x700")
main_window.mainloop()

# This is the final piece that accounts for errors