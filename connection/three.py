import tkinter as tk
import mysql.connector

def fetch_data():
    # Connect to MySQL database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kavya@28245",
        database="bookdatabase"
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute a SELECT query
    cursor.execute("SELECT book_name AS alias1, author AS alias2 FROM table_books")

    # Fetch all rows
    rows = cursor.fetchall()

    # Close cursor and connection
    cursor.close()
    db.close()

    return rows

def display_data():
    data = fetch_data()

    # Create Tkinter window
    root = tk.Tk()

    # Create labels to display data
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            label = tk.Label(root, text=value)
            label.grid(row=i, column=j)

    root.mainloop()

display_data()
