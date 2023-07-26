import requests
from datetime import datetime

USERNAME = "tamtam"
TOKEN = "shotokillua55"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
## Comment out code below because we already created our user and don't have to run code again
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Calories Burned",
    "unit": "Calorie",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
## Calling this response won't work w/o TOKEN (must insert TOKEN via HTTP Header for higher security rather than thru apikey)
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()
### Instead of line above you can retroactively input data for previous days using code below
# today = datetime(year=2023, month=3, day=4)   # update the quantity accordingly
#print(today.strftime("%Y%m%d"))

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many calories did you burn today?: "),
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response)

put_endpoint = f"{pixel_endpoint}/{pixel_config['date']}"

put_config = {
    "quantity": "3000",
}

# response = requests.put(url=put_endpoint, json=put_config, headers=headers)
# print(response.text)

delete_endpoint = f"{put_endpoint}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)


# THIS IS THE LINK: https://pixe.la/v1/users/tamtam/graphs/graph1.html