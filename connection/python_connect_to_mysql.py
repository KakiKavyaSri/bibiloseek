import tkinter as tk
from tkinter import messagebox
import mysql.connector

def connect_to_database():
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kavya@28245",
            database="booksdatabase"
        )
        cursor = db_connection.cursor()
        messagebox.showinfo("Success", "Connected to the database")
        
        # Execute a SELECT query
        cursor.execute("SELECT * FROM table_books")
        rows = cursor.fetchall()
        
        # Close cursor and connection
        cursor.close()
        db_connection.close()
        print("Database connection closed")
        
        # Display data in GUI
        display_data(rows)
        
    except mysql.connector.Error as error:
        messagebox.showerror("Error", "Failed to connect to the database: {}".format(error))

def display_data(data):
    root = tk.Tk()
    root.title("Database Data Display")
    
    # Create a frame
    frame = tk.Frame(root, bg="lightblue")
    frame.pack(fill=tk.BOTH, expand=True)
    
    # Create a label to display data
    label = tk.Label(frame, text="\n".join(str(row) for row in data), bg="lightblue", fg="black")
    label.pack(pady=10)
    
    root.mainloop()

# Create the main window
root = tk.Tk()
root.title("Database Connection Example")

# Button to connect to the database
btn_connect = tk.Button(root, text="Connect to Database", command=connect_to_database)
btn_connect.pack(pady=10)

root.mainloop()
