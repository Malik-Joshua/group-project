import tkinter as tk
from tkinter import messagebox
import re

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")

        # Create main frame
        self.frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
        self.frame.pack(expand=True)

        # Title Label
        self.title_label = tk.Label(
            self.frame,
            text="User Login",
            font=("Helvetica", 24, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Username Label and Entry
        self.username_label = tk.Label(
            self.frame,
            text="Username:",
            font=("Helvetica", 12),
            bg="#f0f0f0"
        )
        self.username_label.grid(row=1, column=0, pady=10, sticky="e")

        self.username_entry = tk.Entry(
            self.frame,
            font=("Helvetica", 12),
            width=25
        )
        self.username_entry.grid(row=1, column=1, pady=10, padx=10)

        # Password Label and Entry
        self.password_label = tk.Label(
            self.frame,
            text="Password:",
            font=("Helvetica", 12),
            bg="#f0f0f0"
        )
        self.password_label.grid(row=2, column=0, pady=10, sticky="e")

        self.password_entry = tk.Entry(
            self.frame,
            show="*",
            font=("Helvetica", 12),
            width=25
        )
        self.password_entry.grid(row=2, column=1, pady=10, padx=10)

        # Login Button
        self.login_button = tk.Button(
            self.frame,
            text="Login",
            command=self.validate_login,
            font=("Helvetica", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            width=15
        )
        self.login_button.grid(row=3, column=0, columnspan=2, pady=20)

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Basic validation
        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        # Example email validation
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, username):
            messagebox.showerror("Error", "Please enter a valid email address")
            return

        # Password validation (minimum 8 characters, at least one number)
        if len(password) < 8 or not any(char.isdigit() for char in password):
            messagebox.showerror(
                "Error",
                "Password must be at least 8 characters long and contain at least one number"
            )
            return

        # Successful login (in a real application, you would verify against a database)
        messagebox.showinfo("Success", "Login successful!")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginForm(root)
    root.mainloop()



