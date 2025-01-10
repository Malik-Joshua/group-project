import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Simple Login Form")
window.geometry("300x200")

# Create and place the username label and entry
username_label = tk.Label(window, text="Username:")
username_label.pack(pady=10)

username_entry = tk.Entry(window)
username_entry.pack()

# Create and place the password label and entry
password_label = tk.Label(window, text="Password:")
password_label.pack(pady=10)

password_entry = tk.Entry(window, show="*")  # show="*" makes the password hidden
password_entry.pack()

# Function to check login
def check_login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Simple validation
    if username == "" or password == "":
        messagebox.showerror("Error", "Please fill in all fields")
    else:
        messagebox.showinfo("Success", "Login successful!")

# Create and place the login button
login_button = tk.Button(window, text="Login", command=check_login)
login_button.pack(pady=20)

# Start the application
window.mainloop()
