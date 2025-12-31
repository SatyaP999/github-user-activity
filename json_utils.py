import json
from pathlib import Path

GITHUB_RESP = Path('github_response.json')

def init_storage():
    if GITHUB_RESP.exists():
        return True
    else:
        return False

def write_to_json(response):
    try:
        if not(init_storage()):
            with open(GITHUB_RESP, 'w') as f:
                json.dump(response, f, indent=4)
    except Exception as e:
        print(f"Error writing github response to json: {e}")
        
def read_from_json():
    githib_resp = []
    try:
        with open(GITHUB_RESP, 'r') as f:
            githib_resp = json.load(f)
        return githib_resp
    except Exception as e:
        print(f"Error reading github response as a python object: {e}")
    