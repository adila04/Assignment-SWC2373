import requests
import os

def sendMessage(tokenData):
    try:
        url = 'https://webexapis.com/v1/rooms'
        headers = {'Authorization': 'Bearer {}'.format(tokenData)}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print("Failed to connect to the server. Please try again.")
            return
        roomData = response.json()
        roomNo = 0
        print("List Room : ")
        for room in roomData["items"]:
            roomNo +=1
            print(f"| {roomNo} | {room['title']}")
        while True:
            try:
                selectedRoomNo = int(input("Room Number : "))
                if 1 <= selectedRoomNo <= len(roomData["items"]):
                    break
                else:
                    print("Invalid room number. Please enter a valid room number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        message = input("Enter your message: ")
        messages_url = 'https://webexapis.com/v1/messages'
        header2 = {
            'Authorization': 'Bearer {}'.format(tokenData),
            'Content-Type': 'application/json'
        }

        params = {'roomId': roomId, 'markdown': message}
        response2 = requests.post(messages_url, headers=header2, json=params)
        if response2.status_code == 200:
            print("Message is already sent to a room!")
            while True:
                print("1.Back To Menu")
                print("2.Exit")
    
                nav = int(input("Enter your option : "))
        
                if nav == 1:
                    return
                elif nav == 2:
                    print("\nExit")
                    os._exit(0)
                else:
                    print("\nInvalid option. Please enter the menu number ")
        else:
            print("\nFailed to connect to the Webex server. Please try again.")
    except Exception as e:
        print("An error occurred:", e)
