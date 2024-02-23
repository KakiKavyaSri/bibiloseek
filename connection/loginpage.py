import tkinter as tk
from tkinter import messagebox
import mysql.connector
import source_code2  # Importing the first page module

def validate_login(root):
    # Connect to the MySQL database
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kavya@28245",
            database="loginpage"
        )
        
        cursor = db_connection.cursor()

        # Get the username and password entered by the user
        username = entry_username.get()
        password = entry_password.get()

        # Query to check if the entered username and password exist in the database
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            root.destroy()  # Close the login window
            source_code2.show_first_page()  # Call the function to show the first page
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    except mysql.connector.Error as error:
        messagebox.showerror("Database Error", "Unable to connect to the database: {}".format(error))

    finally:
        # Close database connection
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()

# Create the main window
root = tk.Tk()
root.title("Login")

# Set window size and position it in the center of the screen
window_width = 600  # Increased width
window_height = 400  # Increased height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) / 2
y_coordinate = (screen_height - window_height) / 2
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

# Create labels and entry widgets for username and password
label_username = tk.Label(root, text="Username:", font=("Helvetica", 20))
label_username.grid(row=0, column=0, padx=20, pady=(50, 40), sticky=tk.W)  # Moved down a little

entry_username = tk.Entry(root, font=("Helvetica", 20))
entry_username.grid(row=0, column=1, padx=20, pady=(50, 40))  # Moved down a little

label_password = tk.Label(root, text="Password:", font=("Helvetica", 20))
label_password.grid(row=1, column=0, padx=20, pady=(50,60), sticky=tk.W)

entry_password = tk.Entry(root, show="*", font=("Helvetica", 20))
entry_password.grid(row=1, column=1, padx=20, pady=(50,60))

# Create a login button
login_button = tk.Button(root, text="Login", font=("Helvetica", 20), command=lambda: validate_login(root))
login_button.grid(row=2, column=0, columnspan=2, pady=20)  # Moved down a little

# Set the font and font size for all widgets
font = ("Helvetica", 14)
root.option_add("*Font", font)

# Set background and foreground colors
root.configure(bg="#f0f0f0")  # Light gray background
root.option_add("*background", "#f0f0f0")
root.option_add("*foreground", "black")

# Run the Tkinter event loop
root.mainloop()
