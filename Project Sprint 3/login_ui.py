import json
import os

# Tkinter UI
import tkinter as tk
from tkinter import messagebox
from maps_api import get_directions
from visualization import plot_food_saved, plot_donor_participation, plot_delivery_efficiency

DB_FILE = "users.json"

def load_users():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(DB_FILE, "w") as f:
        json.dump(users, f)

def get_user(username):
    users = load_users()
    return users.get(username)

def add_user(username, password):
    users = load_users()
    if username in users:
        return False
    users[username] = password
    save_users(users)
    return True

# Tkinter Login/Register UI
def run_tkinter_ui():
    def open_charts_window():
        charts_win = tk.Toplevel(root)
        charts_win.title("FoodWeb Analytics")
        charts_win.geometry("300x150")
        charts_win.configure(bg="#f8fafc")
        tk.Label(charts_win, text="Analytics Dashboard", font=("Arial", 14, "bold"), bg="#f8fafc", fg="#2d6a4f").pack(pady=10)
        charts_btn = tk.Button(charts_win, text="Show Charts", command=show_charts, font=("Arial", 12), bg="#ffb703", fg="black", width=15)
        charts_btn.pack(pady=20)

    def login():
        username = entry_username.get()
        password = entry_password.get()
        user_pw = get_user(username)
        if user_pw and user_pw == password:
            messagebox.showinfo("FoodWeb Login", "Login successful! Welcome to FoodWeb.")
            open_charts_window()
        else:
            messagebox.showerror("FoodWeb Login", "Invalid credentials.")

    def register():
        username = entry_username.get()
        password = entry_password.get()
        if add_user(username, password):
            messagebox.showinfo("FoodWeb Register", "Registration successful! Welcome to FoodWeb.")
            open_charts_window()
        else:
            messagebox.showerror("FoodWeb Register", "Username already exists.")

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


    def show_charts():
        # Example data; replace with real data as needed
        food_saved_data = {'dates': ['2025-07-01','2025-07-02','2025-07-03'], 'amounts': [120, 150, 100]}
        donor_data = {'donors': ['Genji','Casey','Dane'], 'donations': [5, 8, 3]}
        efficiency_data = {'dates': ['2025-07-01','2025-07-02','2025-07-03'], 'delivery_times': [30, 25, 40]}
        plot_food_saved(food_saved_data)
        plot_donor_participation(donor_data)
        plot_delivery_efficiency(efficiency_data)

    # ...existing code...

    root.mainloop()

# Entry point
if __name__ == "__main__":
    run_tkinter_ui()
