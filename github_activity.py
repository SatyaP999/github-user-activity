import requests

GITHUB_API_URL = f"https://api.github.com"

def get_events(username):
    try:
        endpoint = f"{GITHUB_API_URL}/users/{username}/events"
        print(endpoint)
        response = requests.get(endpoint)
        # print(response)
        if response.status_code == 200:
            events = response.json()
            print(f"Successfully fetched {len(events)} public events.")
            if events:
                print(f"First event type: {events[0]}")
            else:
                print(f"Failed to retrieve events. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error getting response: {e}")
        