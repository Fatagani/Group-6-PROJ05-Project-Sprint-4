# ui_show_models.py
# Simple Tkinter UI to display basic model data

import tkinter as tk
from tkinter import ttk
from models.models import User, Category, FoodItem, Report
from datetime import datetime

class ModelViewer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Model Viewer")
        self.geometry("600x400")
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TNotebook.Tab", font=("Arial", 12, "bold"))
        style.configure("TLabel", font=("Arial", 12), background="#f8f8ff")
        style.configure("Header.TLabel", font=("Arial", 16, "bold"), background="#e6e6fa", foreground="#333366")

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=20, pady=20)

        # User Tab
        user_tab = tk.Frame(notebook, bg="#f8f8ff")
        notebook.add(user_tab, text="User")
        user = User(username="alice", password_hash="hash123", email="alice@example.com", role="admin")
        self.display_header(user_tab, "User Model")
        self.display_dict(user_tab, user.to_dict())

        # Category Tab
        category_tab = tk.Frame(notebook, bg="#f8f8ff")
        notebook.add(category_tab, text="Category")
        category = Category(name="Fruit", description="Edible sweet plant product")
        self.display_header(category_tab, "Category Model")
        self.display_dict(category_tab, category.to_dict())

        # FoodItem Tab
        food_tab = tk.Frame(notebook, bg="#f8f8ff")
        notebook.add(food_tab, text="FoodItem")
        nutrients = {"calories": 52, "protein": 0.3, "fat": 0.2, "carbs": 14}
        food_item = FoodItem(name="Apple", category="Fruit", nutrients=nutrients, created_by=user._id)
        self.display_header(food_tab, "FoodItem Model")
        self.display_dict(food_tab, food_item.to_dict())

        # Report Tab
        report_tab = tk.Frame(notebook, bg="#f8f8ff")
        notebook.add(report_tab, text="Report")
        report_data = {"summary": "Good nutritional value."}
        report = Report(user_id=user._id, food_item_id=food_item._id, report_type="nutrition", data=report_data, created_at=datetime.utcnow())
        self.display_header(report_tab, "Report Model")
        self.display_dict(report_tab, report.to_dict())

    def display_header(self, parent, text):
        header = ttk.Label(parent, text=text, style="Header.TLabel")
        header.grid(row=0, column=0, columnspan=2, pady=(10, 20), padx=10, sticky="ew")

    def display_dict(self, parent, data):
        for i, (key, value) in enumerate(data.items()):
            ttk.Label(parent, text=f"{key}:", font=("Arial", 12, "bold"), background="#f8f8ff").grid(row=i+1, column=0, sticky="e", padx=20, pady=8)
            ttk.Label(parent, text=str(value), font=("Arial", 12), background="#f8f8ff").grid(row=i+1, column=1, sticky="w", padx=20, pady=8)

if __name__ == "__main__":
    app = ModelViewer()
    app.mainloop()
