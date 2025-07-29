# launcher_ui.py
"""
Launcher UI for FoodWeb
Allows user to choose between Login UI (Tkinter) and Donor/Recipient Portal (Flet).
"""
import tkinter as tk
import subprocess

def run_login_ui():
    subprocess.Popen(["python", "login_ui.py"])

def run_flet_ui():
    subprocess.Popen(["python", "flet_ui.py"])

def main():
    root = tk.Tk()
    root.title("FoodWeb Launcher")
    root.geometry("300x180")
    root.configure(bg="#f8fafc")

    tk.Label(root, text="FoodWeb Portal", font=("Arial", 18, "bold"), fg="#2d6a4f", bg="#f8fafc").pack(pady=20)
    tk.Button(root, text="Login UI (Tkinter)", command=run_login_ui, font=("Arial", 12), bg="#2d6a4f", fg="white", width=20).pack(pady=10)
    tk.Button(root, text="Donor/Recipient Portal (Flet)", command=run_flet_ui, font=("Arial", 12), bg="#40916c", fg="white", width=20).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
