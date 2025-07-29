# visualization.py
"""
Matplotlib visualizations for food saved, donor participation, and delivery efficiency.
"""
import matplotlib.pyplot as plt

def plot_food_saved(food_saved_data):
    plt.figure(figsize=(6,4))
    plt.plot(food_saved_data['dates'], food_saved_data['amounts'], marker='o')
    plt.title('Food Saved Over Time')
    plt.xlabel('Date')
    plt.ylabel('Food Saved (kg)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_donor_participation(donor_data):
    plt.figure(figsize=(6,4))
    plt.bar(donor_data['donors'], donor_data['donations'])
    plt.title('Donor Participation')
    plt.xlabel('Donor')
    plt.ylabel('Donations (kg)')
    plt.tight_layout()
    plt.show()

def plot_delivery_efficiency(efficiency_data):
    plt.figure(figsize=(6,4))
    plt.plot(efficiency_data['dates'], efficiency_data['delivery_times'], marker='x', color='green')
    plt.title('Delivery Efficiency Over Time')
    plt.xlabel('Date')
    plt.ylabel('Delivery Time (minutes)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Example data
    food_saved_data = {'dates': ['2025-07-01','2025-07-02','2025-07-03'], 'amounts': [120, 150, 100]}
    donor_data = {'donors': ['Alice','Bob','Carol'], 'donations': [5, 8, 3]}
    efficiency_data = {'dates': ['2025-07-01','2025-07-02','2025-07-03'], 'delivery_times': [30, 25, 40]}
    plot_food_saved(food_saved_data)
    plot_donor_participation(donor_data)
    plot_delivery_efficiency(efficiency_data)
