import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

# Database connection
conn = mysql.connector.connect(host='localhost', username='root', password='Kavya@28245', database='loginpage')
my_cursor = conn.cursor()

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Check if the provided username and password match the specified values
    if (username == "user1" and password == "pass@123") or (username == "user2" and password == "pass@234"):
        messagebox.showinfo("Success", "You have successfully logged in.")
    else:
        messagebox.showerror("Error", "Invalid username or password.")

# Create main window
root = tk.Tk()
root.title("Login Page")

# Load and display background image
bg_image = Image.open("C:/Users/LENOVO/Pictures/TOU.jpg")
bg_image = bg_image.resize((820, 820))
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(root, image=bg_photo)
background_label.place(x=0, y=-100, relwidth=1, relheight=1)

# Username entry
username_label = tk.Label(root, text="Username:", bg='white')
username_label.place(relx=0.5, rely=0.4, anchor='center')
username_entry = tk.Entry(root)
username_entry.place(relx=0.6, rely=0.4, anchor='center')

# Password entry
password_label = tk.Label(root, text="Password:", bg='white')
password_label.place(relx=0.5, rely=0.5, anchor='center')
password_entry = tk.Entry(root, show="*")
password_entry.place(relx=0.6, rely=0.5, anchor='center')

# Login button
login_button = tk.Button(root, text="Login", command=login)
login_button.place(relx=0.5, rely=0.6, anchor='center')

root.mainloop()

# Closing the database connection
conn.close()
