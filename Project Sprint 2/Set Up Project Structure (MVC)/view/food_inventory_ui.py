import tkinter as tk
from tkinter import messagebox, ttk
from model.food_inventory import add_food, get_food, update_quantity, list_foods

class FoodInventoryUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Inventory Management")
        self.root.geometry("600x400")
        self.root.configure(bg="#f8fafc")

        # Add Food Section
        add_frame = tk.LabelFrame(root, text="Add Food Item", bg="#f8fafc", font=("Arial", 12, "bold"))
        add_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(add_frame, text="Name:", bg="#f8fafc").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(add_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_frame, text="Category:", bg="#f8fafc").grid(row=0, column=2, padx=5, pady=5)
        self.category_entry = tk.Entry(add_frame)
        self.category_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(add_frame, text="Price:", bg="#f8fafc").grid(row=1, column=0, padx=5, pady=5)
        self.price_entry = tk.Entry(add_frame)
        self.price_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_frame, text="Quantity:", bg="#f8fafc").grid(row=1, column=2, padx=5, pady=5)
        self.quantity_entry = tk.Entry(add_frame)
        self.quantity_entry.grid(row=1, column=3, padx=5, pady=5)

        add_btn = tk.Button(add_frame, text="Add Food", command=self.add_food, bg="#2d6a4f", fg="white")
        add_btn.grid(row=2, column=0, columnspan=4, pady=10)

        # Food List Section
        list_frame = tk.LabelFrame(root, text="Food Inventory", bg="#f8fafc", font=("Arial", 12, "bold"))
        list_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.food_tree = ttk.Treeview(list_frame, columns=("Name", "Category", "Price", "Quantity"), show="headings")
        self.food_tree.heading("Name", text="Name")
        self.food_tree.heading("Category", text="Category")
        self.food_tree.heading("Price", text="Price")
        self.food_tree.heading("Quantity", text="Quantity")
        self.food_tree.pack(fill="both", expand=True)

        update_frame = tk.Frame(root, bg="#f8fafc")
        update_frame.pack(fill="x", padx=10, pady=5)
        tk.Label(update_frame, text="Update Quantity for Selected Food:", bg="#f8fafc").pack(side="left", padx=5)
        self.update_quantity_entry = tk.Entry(update_frame, width=10)
        self.update_quantity_entry.pack(side="left", padx=5)
        update_btn = tk.Button(update_frame, text="Update Quantity", command=self.update_quantity, bg="#40916c", fg="white")
        update_btn.pack(side="left", padx=5)

        self.refresh_food_list()

    def add_food(self):
        name = self.name_entry.get()
        category = self.category_entry.get()
        try:
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Price must be a number and quantity must be an integer.")
            return
        if add_food(name, category, price, quantity):
            messagebox.showinfo("Success", "Food item added.")
            self.refresh_food_list()
        else:
            messagebox.showerror("Error", "Failed to add food item. Name may already exist.")

    def refresh_food_list(self):
        for row in self.food_tree.get_children():
            self.food_tree.delete(row)
        for food in list_foods():
            self.food_tree.insert("", "end", values=(food['name'], food['category'], food['price'], food['quantity']))

    def update_quantity(self):
        selected = self.food_tree.selection()
        if not selected:
            messagebox.showerror("Error", "No food item selected.")
            return
        name = self.food_tree.item(selected[0])['values'][0]
        try:
            quantity = int(self.update_quantity_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Quantity must be an integer.")
            return
        if update_quantity(name, quantity):
            messagebox.showinfo("Success", "Quantity updated.")
            self.refresh_food_list()
        else:
            messagebox.showerror("Error", "Failed to update quantity.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FoodInventoryUI(root)
    root.mainloop()
