import listsRooms as room
import listMarkdownMessage as mark

if __name__ == "__main__":
    
    access_token = 'Zjg0YjM1ZmMtZDUzMi00MWI5LTg5ZDQtM2Q0NWIyNmRiYTQxZDExNjExZWEtNDky_P0A1_d2c22ef8-905b-4ab9-b9c6-81bc98924b65'
    headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
    }
    roomId = room.get_room_id(input("room's name : "), headers)
    while True:
        message = mark.get_message(roomId, headers)     
        if message.startswith("/"):
            mark.send_message(message, roomId, headers)
        else:
            print(message)
