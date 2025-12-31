import requests
from json_utils import *

GITHUB_API_URL = f"https://api.github.com"

def get_events(username):
    try:
        endpoint = f"{GITHUB_API_URL}/users/{username}/events"
        print(endpoint)
        response = requests.get(endpoint)
        # print(response)
        if response.status_code == 200:
            events = response.json()
            write_to_json(response=events)
            print(f"Successfully fetched {len(events)} public events.")
            # if events:
            #     print(f"First event type: {events[0]}")
            # else:
            #     print(f"Failed to retrieve events. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error getting response: {e}")
        
def print_user_activity():
    try:
        events_lst = read_from_json()
        for event in events_lst:
            repo_name = event["repo"]["name"]
            if event["type"] == "PushEvent":
                print(f"- Pushed to {repo_name} \n")
            elif event["type"] == "CreateEvent":
                ref_type = event["payload"]["ref_type"]
                print(f"- Created a {ref_type} in {repo_name} \n")
            else:
                event_type = event["type"]
                print(f"- {event_type} in {repo_name}")
    except Exception as e:
        print(f"Error printing user activity: {e}")
            
        