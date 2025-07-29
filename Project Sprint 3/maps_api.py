# maps_api.py
"""
Google Maps API integration for geocoding and directions.
Requires: requests
Get your API key from Google Cloud Platform and set it below.
"""
import requests

API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"  # Replace with your actual API key

GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
DIRECTIONS_URL = "https://maps.googleapis.com/maps/api/directions/json"

def geocode_address(address):
    params = {"address": address, "key": API_KEY}
    response = requests.get(GEOCODE_URL, params=params)
    data = response.json()
    if data["status"] == "OK":
        location = data["results"][0]["geometry"]["location"]
        return location["lat"], location["lng"]
    else:
        return None

def get_directions(origin, destination):
    params = {"origin": origin, "destination": destination, "key": API_KEY}
    response = requests.get(DIRECTIONS_URL, params=params)
    data = response.json()
    if data["status"] == "OK":
        route = data["routes"][0]["legs"][0]
        steps = [step["html_instructions"] for step in route["steps"]]
        return steps
    else:
        return None

if __name__ == "__main__":
    # Example usage
    address = "1600 Amphitheatre Parkway, Mountain View, CA"
    coords = geocode_address(address)
    print(f"Coordinates for {address}: {coords}")

    origin = "New York, NY"
    destination = "Boston, MA"
    directions = get_directions(origin, destination)
    print(f"Directions from {origin} to {destination}:")
    for step in directions or []:
        print(step)
