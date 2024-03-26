import requests, os

def createWebexRoom(tokenData):
    try:
        url = 'https://webexapis.com/v1/rooms'
        headers = {
            'Authorization' : 'Bearer {}'.format(tokenData),
            'Content-Type': 'application/json'
        }
        roomName = input("\nEnter your room name : ")
        params = { 'title' : roomName }
        response = requests.post(url, headers=headers, json=params)
        if response.status_code == 200:
            print("Room Successfully created in Webex ! ")
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
                     print("\n Invalid option.Please try again ")
        else:
            print("\nFailed to create the room. Please try again.")
    except Exception as e:
        print("An error occurred :", e)
