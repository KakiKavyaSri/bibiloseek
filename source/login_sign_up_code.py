import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#f0f0f0")
        self.controller = controller

        label = tk.Label(self, text="Login", font=("Arial", 24), bg="#f0f0f0", fg="#333")
        label.pack(pady=10)

        self.username_entry = tk.Entry(self, font=("Arial", 14), bg="#fff", fg="#333")
        self.username_entry.pack(ipady=5, padx=20, pady=5, fill=tk.X)

        self.password_entry = tk.Entry(self, font=("Arial", 14), show="*", bg="#fff", fg="#333")
        self.password_entry.pack(ipady=5, padx=20, pady=5, fill=tk.X)

        login_button = tk.Button(self, text="Login", font=("Arial", 14), bg="#007bff", fg="#fff",
                                 activebackground="#0056b3", activeforeground="#fff", bd=0,
                                 command=self.login)
        login_button.pack(pady=10, ipadx=10)

        signup_button = tk.Button(self, text="Sign Up", font=("Arial", 14), bg="#28a745", fg="#fff",
                                  activebackground="#218838", activeforeground="#fff", bd=0,
                                  command=lambda: controller.show_frame(SignupPage))
        signup_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Placeholder authentication
        if username == "user" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            # Placeholder: redirect to main application
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")


class SignupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#f0f0f0")
        self.controller = controller

        label = tk.Label(self, text="Sign Up", font=("Arial", 24), bg="#f0f0f0", fg="#333")
        label.pack(pady=10)

        self.username_entry = tk.Entry(self, font=("Arial", 14), bg="#fff", fg="#333")
        self.username_entry.pack(ipady=5, padx=20, pady=5, fill=tk.X)

        self.password_entry = tk.Entry(self, font=("Arial", 14), show="*", bg="#fff", fg="#333")
        self.password_entry.pack(ipady=5, padx=20, pady=5, fill=tk.X)

        signup_button = tk.Button(self, text="Sign Up", font=("Arial", 14), bg="#007bff", fg="#fff",
                                  activebackground="#0056b3", activeforeground="#fff", bd=0,
                                  command=self.signup)
        signup_button.pack(pady=10, ipadx=10)

        login_button = tk.Button(self, text="Login", font=("Arial", 14), bg="#28a745", fg="#fff",
                                 activebackground="#218838", activeforeground="#fff", bd=0,
                                 command=lambda: controller.show_frame(LoginPage))
        login_button.pack()

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Placeholder: save username and password
        messagebox.showinfo("Sign Up Successful", "Account created for " + username)
        self.controller.show_frame(LoginPage)


class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Login System")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginPage, SignupPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
