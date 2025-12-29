import sys
from github_activity import *
def main():
    if len(sys.argv) == 2:
        if len(sys.argv[-1]) != 0:
            user_name = sys.argv[-1]
            print(f"Fetching activity for {sys.argv[-1]}")
            get_events(username=user_name)
        else:
            print(f"Please provide a username..")



if __name__ == "__main__":
    main()
    
    