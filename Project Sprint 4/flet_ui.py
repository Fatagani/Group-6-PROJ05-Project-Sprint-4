# flet_ui.py
"""
Flet UI for Donors and Recipients
Allows donors to submit donations and recipients to request pickups.
"""
import flet as ft
import requests

API_URL = "http://127.0.0.1:8000"

# Donor Page
class DonorPage(ft.UserControl):
    def build(self):
        self.donor = ft.TextField(label="Donor Name", width=300)
        self.food_type = ft.TextField(label="Food Type", width=300)
        self.amount = ft.TextField(label="Amount (kg)", width=300)
        self.location = ft.TextField(label="Location", width=300)
        self.status = ft.Text("", color="green", size=16)
        donate_btn = ft.ElevatedButton("Donate", on_click=self.donate, style=ft.ButtonStyle(bgcolor="#2d6a4f", color="white"), width=150)
        return ft.Container(
            content=ft.Column([
                ft.Text("Donor - Submit Donation", size=24, weight="bold", color="#2d6a4f"),
                self.donor,
                self.food_type,
                self.amount,
                self.location,
                donate_btn,
                self.status
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=30,
            bgcolor="#f8fafc",
            border_radius=20,
            alignment=ft.alignment.center
        )
    def donate(self, e):
        data = {
            "donor": self.donor.value,
            "food_type": self.food_type.value,
            "amount": float(self.amount.value),
            "location": self.location.value
        }
        resp = requests.post(f"{API_URL}/donate", json=data)
        if resp.status_code == 200:
            self.status.value = "Donation submitted!"
        else:
            self.status.value = f"Error: {resp.text}"
        self.update()

# Recipient Page
class RecipientPage(ft.UserControl):
    def build(self):
        self.volunteer = ft.TextField(label="Recipient Name", width=300)
        self.pickup_location = ft.TextField(label="Pickup Location", width=300)
        self.delivery_location = ft.TextField(label="Delivery Location", width=300)
        self.food_type = ft.TextField(label="Food Type", width=300)
        self.amount = ft.TextField(label="Amount (kg)", width=300)
        self.status = ft.Text("", color="blue", size=16)
        pickup_btn = ft.ElevatedButton("Request Pickup", on_click=self.pickup, style=ft.ButtonStyle(bgcolor="#40916c", color="white"), width=150)
        return ft.Container(
            content=ft.Column([
                ft.Text("Recipient - Request Pickup", size=24, weight="bold", color="#40916c"),
                self.volunteer,
                self.pickup_location,
                self.delivery_location,
                self.food_type,
                self.amount,
                pickup_btn,
                self.status
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=30,
            bgcolor="#f8fafc",
            border_radius=20,
            alignment=ft.alignment.center
        )
    def pickup(self, e):
        data = {
            "volunteer": self.volunteer.value,
            "pickup_location": self.pickup_location.value,
            "delivery_location": self.delivery_location.value,
            "food_type": self.food_type.value,
            "amount": float(self.amount.value)
        }
        resp = requests.post(f"{API_URL}/pickup", json=data)
        if resp.status_code == 200:
            self.status.value = "Pickup requested!"
        else:
            self.status.value = f"Error: {resp.text}"
        self.update()

# Main App
def main(page: ft.Page):
    page.title = "FoodWeb - Donor & Recipient Portal"
    page.bgcolor = "#e9ecef"
    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="Donor", content=DonorPage()),
            ft.Tab(text="Recipient", content=RecipientPage())
        ]
    )
    page.add(ft.Container(content=tabs, alignment=ft.alignment.center, padding=40))

if __name__ == "__main__":
    ft.app(target=main)
