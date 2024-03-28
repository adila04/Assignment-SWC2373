import requests, os

def listRoomData(tokenData):
    url = 'https://webexapis.com/v1/rooms'
    headers = {
            'Authorization': 'Bearer {}'.format(tokenData),
             'Content-Type': 'application/json'
             }
    params={'max': '100'}
    res = requests.get(url, headers=headers, params=params) 
    if res.status_code == 200:
       rooms = res.json()['items']
       print("List Rooms: ")
       count = min(len(rooms), 5)
       for i in range(count):
           room=rooms[i]
           print(f"Room {i+1}:")
           print("Room Id:",room["id"])
           print("Room Title:",room["title"])
           print("Date Created:",room["created"])
           print("Last Activity:",room["lastActivity"])
       else:
          print("Failed to display list room.")
