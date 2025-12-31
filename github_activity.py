import requests
from collections import defaultdict
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

def print_event_summary():
    try:
        even_lst = read_from_json()
        event_dict = defaultdict(int)
        for event in even_lst:
            if event["type"] == "PushEvent":
                repo_name = event['repo']["name"]
                event_dict[("Pushed", repo_name)] += 1
            elif event["type"] == "CreateEvent":
                repo_name = event['repo']["name"]
                ref_type = event["payload"]["ref_type"]
                event_dict[(f"Created a {ref_type} in", repo_name)] += 1
            else:
                repo_name = event['repo']["name"]
                event_type = event["type"]
                event_dict[(event_type, repo_name)] += 1
        
        for key in event_dict.keys():
            if key[0] == "Pushed":
                print(f"- {key[0]} {event_dict[key]} times in {key[1]}")
            elif "Created" in key[0]:
                print(f"- {key[0]} {key[1]} {event_dict[key]} times.")
            
    except Exception as e:
        print(f"Error in method print_event_summary: {e}")