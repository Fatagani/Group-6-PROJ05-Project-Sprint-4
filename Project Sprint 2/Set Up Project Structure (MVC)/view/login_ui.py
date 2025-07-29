import json
import os

# Tkinter UI
import tkinter as tk
from tkinter import messagebox

from controller.login_bl import authenticate, register_user
from view.food_inventory_ui import FoodInventoryUI

DB_FILE = "users.json"

def run_tkinter_ui():
    def login():
        username = entry_username.get()
        password = entry_password.get()
        success, msg = authenticate(username, password)
        if success:
            messagebox.showinfo("FoodWeb Login", msg)
        else:
            messagebox.showerror("FoodWeb Login", msg)

    def register():
        username = entry_username.get()
        password = entry_password.get()
        success, msg = register_user(username, password)
        if success:
            messagebox.showinfo("FoodWeb Register", msg)
            # Open Food Inventory UI after successful registration
            root.destroy()
            inv_root = tk.Tk()
            app = FoodInventoryUI(inv_root)
            inv_root.mainloop()
        else:
            messagebox.showerror("FoodWeb Register", msg)

    root = tk.Tk()
    root.title("FoodWeb")
    root.geometry("350x250")
    root.configure(bg="#f8fafc")

    # FoodWeb branding
    title_label = tk.Label(root, text="FoodWeb", font=("Arial", 20, "bold"), fg="#2d6a4f", bg="#f8fafc")
    title_label.pack(pady=(20, 10))

    frame = tk.Frame(root, bg="#f8fafc")
    frame.pack(pady=10)

    tk.Label(frame, text="Username:", font=("Arial", 12), bg="#f8fafc").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    entry_username = tk.Entry(frame, font=("Arial", 12), width=20)
    entry_username.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame, text="Password:", font=("Arial", 12), bg="#f8fafc").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entry_password = tk.Entry(frame, font=("Arial", 12), show="*", width=20)
    entry_password.grid(row=1, column=1, padx=5, pady=5)

    btn_frame = tk.Frame(root, bg="#f8fafc")
    btn_frame.pack(pady=10)
    login_btn = tk.Button(btn_frame, text="Login", command=login, font=("Arial", 12), bg="#2d6a4f", fg="white", width=10)
    login_btn.grid(row=0, column=0, padx=10)
    register_btn = tk.Button(btn_frame, text="Register", command=register, font=("Arial", 12), bg="#40916c", fg="white", width=10)
    register_btn.grid(row=0, column=1, padx=10)

    root.mainloop()

# Entry point
if __name__ == "__main__":
    run_tkinter_ui()
