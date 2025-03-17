import requests

'''
Requests - third party library for sending an receiving data

uv add requests...

Steps:
1. Creating a folder per lab/assignment/project/application
2. Inside folder: uv init, uv venv - creates uv repor and uv virtual environment
    - powershell -ExecutionPolicy ByPass -c .venv/Scripts/activate
    - uv add requests colorama

3. File > Open Folder and ensure you just have the folder with your code open in the VSCode explorer.
'''

'''
HTTP Methods

GET -> getting data from a server
POST -> sending data to a server
PUT -> sending data to a server (different way)
DELETE -> delete something on a server


'''

response = requests.get('https://jsonplaceholder.typicode.com/users')
print(response)

# NOTE: the variable response is NOT the JSON data - 
# it is a Response object that "contains" the data as well as other information


'''
HTTP Status Codes

200-299 -> success
300-399 -> file/resources that have been moves
400-499 -> 404 not found
500-599 -> application errors/server-side errors

'''

if response.status_code == 200:
    # request was successful
    data = response.json() # extracts the data
    print(data)