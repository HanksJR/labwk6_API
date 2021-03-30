import requests
import mapquest as maps

def get_message(id, headers):
    url = "https://webexapis.com/v1/messages"
    params = {"roomId": id, "max":1}
    json_data = requests.get(url, headers=headers, params=params).json()
    return json_data["items"][0]["text"]

def send_message(text, id, headers):
    url = "https://webexapis.com/v1/messages"
    message = "In {} ISS will fly over on {} for {} seconds".format(text[1:], str(maps.iss(maps.mapping(text))[1]), str(maps.iss(maps.mapping(text))[0]))
    params = {"roomId": id, "markdown": message}
    requests.post(url, headers=headers, json=params)

