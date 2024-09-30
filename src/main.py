import requests
import argparse
from dotenv import load_dotenv
import os

BASE_URL = "https://maps.googleapis.com/maps/api/directions/json?"

load_dotenv()
API_KEY = os.getenv('API_KEY')


def get_route(origin, destination):
    # Setze den Modus auf 'transit'
    mode = 'transit'
    url = f'{BASE_URL}origin={origin}&destination={destination}&mode={mode}&key={API_KEY}&departure_time=now'

    response = requests.get(url)
    route_data = response.json()

    if route_data['status'] == 'OK':
        route = route_data['routes'][0]
        leg = route['legs'][0]
        return {
            'distance': leg['distance']['text'],
            'duration': leg['duration']['text'],
            'start_address': leg['start_address'],
            'end_address': leg['end_address'],
            'steps': leg['steps']
        }
    else:
        if not os.getenv('TEST_MODE'):
            print(f"Error fetching route: {route_data['status']}")
        return None




def get_args():
    parser = argparse.ArgumentParser(description="Real-Time Traffic-Based Navigation")
    parser.add_argument('origin', type=str, help="Origin address (e.g., 'New York, NY')")
    parser.add_argument('destination', type=str, help="Destination address (e.g., 'Boston, MA')")
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    origin = args.origin
    destination = args.destination

    route = get_route(origin, destination)
    if route:
        print(f"From: {route['start_address']}")
        print(f"To: {route['end_address']}")
        print(f"Distance: {route['distance']}")
        print(f"Duration with traffic: {route['duration']}")
        print("\nDirections:")
        for step in route['steps']:
            print(step['html_instructions'])
