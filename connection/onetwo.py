import tkinter as tk
from tkinter import messagebox
import mysql.connector

def search_database(book_name, author, root):
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kavya@28245",
            database="booksdatabase"
        )
        cursor = db_connection.cursor()
        
        # Execute a SELECT query to search for the book
        cursor.execute("SELECT * FROM table_books WHERE book_name = %s AND author = %s", (book_name, author))
        row = cursor.fetchone()
        
        # Close cursor and connection
        cursor.close()
        db_connection.close()
        print("Database connection closed")
        
        if row:
            # If book found, display all values of that row
            display_data(row)
            # Close the main window
            root.destroy()
        else:
            # If book not found, show message box
            messagebox.showinfo("Book Not Found", "The book '{}' by '{}' was not currently present in our Library.\nTHANK YOU🙏".format(book_name, author))
        
    except mysql.connector.Error as error:
        messagebox.showerror("Error", "Failed to connect to the database: {}".format(error))

def display_data(data):
    root = tk.Tk()
    root.title("Book Details")
    
    # # Background image
    # background_image = tk.PhotoImage(file="../assets/libblurimage.png")
    # background_label = tk.Label(root, image=background_image)
    # background_label.place(relwidth=1, relheight=1)
    
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Calculate the x and y coordinates to center the window
    x = (screen_width - 800) / 2
    y = (screen_height - 600) / 2
    
    # Set the position of the window
    root.geometry(f"1000x600+{int(x)}+{int(y)}")
    
    # Create a frame
    frame = tk.Frame(root, bg="lightblue", width=800, height=600)
    frame.pack(fill=tk.BOTH, expand=True)
    
    # Display all values of the row with larger font size and column names
    labels = [("Book ID", data[0]), 
              ("Book Name", data[1]), 
              ("Author", data[2]), 
              ("Genre", data[3]), 
              ("Number of Copies", data[4]), 
              ("Average Ratings", data[5]),
              ("Books Section", data[6])]  # Change this to the actual column name
              
    for i, (column_name, value) in enumerate(labels):
        label_name = tk.Label(frame, text=f"{column_name}:", bg="lightblue", fg="black", font=("Arial", 30))  # Adjust font size here
        label_name.grid(row=i, column=0, padx=(50,10), pady=10, sticky="w")
        label_value = tk.Label(frame, text=str(value), bg="lightblue", fg="black", font=("Arial", 30))  # Adjust font size here
        label_value.grid(row=i, column=1, padx=(10,50), pady=10, sticky="w")
    
    # Create a back button
    btn_back = tk.Button(root, text="BACK", command=root.destroy, font=("Arial", 20), bg="black", fg="white", width=20)
    btn_back.pack(side=tk.BOTTOM, pady=20)
    
    root.mainloop()

# Create the main window
root = tk.Tk()
root.title("Book Search")

# Background image
background_image = tk.PhotoImage(file="../assets/libblurimage.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x = (screen_width - 500) / 2
y = (screen_height - 400) / 2

# Set the position of the window
root.geometry(f"500x400+{int(x)}+{int(y)}")

# Labels and Entry fields for Book Name and Author
tk.Label(root, text="Book Name:", font=("Arial", 20)).pack(pady=(50, 10))
entry_book_name = tk.Entry(root, font=("Arial", 20))
entry_book_name.pack(pady=10)

tk.Label(root, text="Author:", font=("Arial", 20)).pack()
entry_author = tk.Entry(root, font=("Arial", 20))
entry_author.pack()

# Button to search the database
btn_search = tk.Button(root, text="Search", command=lambda: search_database(entry_book_name.get(), entry_author.get(), root), bg="green", fg="white", font=("Arial", 20))
btn_search.pack(pady=(20, 50))

root.mainloop()
