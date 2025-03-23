import json
import requests
import sys
import time
from colorama import Fore

def get_choice(message, data):
    # return choice if numeric and choice is valid
    # use try/except to catch invalid type, no .isdigit(), .isnumeric() etc.

    print("")
    for x in message:
        print(x)

    while True:

        choice = input("\nSelect a user: ")
        print("")

        try:
            choice = int(choice)
            
            if choice == 0:
                choice += data[choice+11]
            else:
                return data[choice - 1]
            
        except IndexError:
            print("\nPlease choose a number within the given numbers.")
        
        except ValueError:
            print("\nPlease enter a digit.")



def run(data):
    time.sleep(0.5)
    current_user = None
    message_list = []
    disp = 1
    if current_user == None:
        for x in data:
            mes = f"{disp}.{x['name']}"
            message_list.append(mes)
            disp += 1
        
        current_user = get_choice(message_list, data)
        
        for key, value in current_user.items():
            if type(value) == str:
                print(f"{key}: {value}")
    
    while True:
        keep_going = input("\nEnter 'c' to continue or enter 'q' to exit: ")

        if keep_going == 'c':
            return False
        elif keep_going == 'q':
            print(Fore.RED + "Exiting now. Goodbye!" + Fore.RESET)
            sys.exit() 

    

    """
    - loop
    - display user names if no current user, and prompt for which user to load
    - if current user, display all attributes whose value is a string, and prompt for which attribute to read
    - after displaying attribute, reset current user
    """

def load():
    data = []
    try:
        with open('db.json', 'r') as f:
            data = json.load(f)
            print(Fore.YELLOW + "Reading data from file..." + Fore.RESET)
    except FileNotFoundError as fnf:
        print("File does not exist... Creating file now...")
        time.sleep(1)
        info = requests.get("https://jsonplaceholder.typicode.com/users")
        data = info.json()

        with open('db.json', 'w') as d:
            json.dump(data, d, indent=4)
            
        print(Fore.GREEN + "File created!" + Fore.RESET)


    """
    - if db.json exists, read data from it
    - if db.json does not exist, fetch it (from https://jsonplaceholder.typicode.com/users)
        using the requests library and create the file
    - prevent possible errors with try/except
    - NO generic exceptions allowed, and give feedback to the user if necessary
    - indicate to the user in yellow whether the data is being read from file or fetched 
    - no pathlib, no os module
    """

    print(Fore.YELLOW + 'Initializing application...' + Fore.RESET)
    time.sleep(1)
    while True:
        run(data)

if __name__ == '__main__':
    # use try/except to allow the program to exit gracefully if ctrl-c used
    try:
        load()
    except KeyboardInterrupt:
        print("\n\nExiting now, goodbye!")