# Fill in this file with the rooms/spaces listing code from the Webex Teams exercise
import requests


def get_room_id(name, headers):
    url_room = "https://webexapis.com/v1/rooms"
    json_data = requests.get(url_room, headers=headers).json()
    for i in json_data["items"]:
        if i["title"] == name:
            return i["id"]

def get_list_room(headers):
    url_list_room = "https://webexapis.com/v1/rooms"
    json_data = requests.get(url_list_room, headers=headers).json()
    print("list of rooms:")
    for i in json_data["items"]:
        print("-", i["title"])