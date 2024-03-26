import requests
import os

from option1 import connectData
from option2 import userInfo
from option3 import listRoomData
from option4 import createWebexRoom
from option5 import sendMessage

def get_user_input(prompt):
    return input(prompt).strip()

def display_menu():
    print("MENU :- ")
    print("0.Test Connection To Webex")
    print("1.Fetch User Data")
    print("2.Fetch Room Data")
    print("3.Create Room")
    print("4.Send Message To Room")
    print("5.Exit")
try:
    tokenData = ""
    while True:
        tokenData = get_user_input("Enter your token: ")
        url = 'https://webexapis.com/v1/people/me'
        headers = {'Authorization': 'Bearer {}'.format(tokenData)}

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            break
        else:
            print("\nFailed to connect to Webex server. Please try again.")

    while True:
        display_menu()
        
        try:
            select = int(get_user_input("Enter your Option : "))

            if select == 0:
                connectData(tokenData)
            elif select == 1:
                userInfo(tokenData)
            elif select == 2:
                listRoomData(tokenData)
            elif select == 3:
                createWebexRoom(tokenData)
            elif select == 4:
                sendMessage(tokenData)
            elif select == 5:
                print("\nExit")
                os._exit(0)
            else:
                print("\nInvalid choice. Please enter a number between 0 and 5.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")
except Exception as e:
    print("\nAn error occurred:", e)
