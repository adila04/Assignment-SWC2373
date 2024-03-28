import requests, os

def userInfo(tokenData):
    try:
        url = 'https://webexapis.com/v1/people/me'
        headers = {
            'Authorization' : 'Bearer {}'.format(tokenData)
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            webexUser = response.json()
            print("Successfully fetch user data !")
            print("User Information:")
            print("User Name: " + webexUser["displayName"])
            print("Nickname: " + webexUser["nickName"])
            print("Email: " + webexUser["emails"][0])

            while True:
                print("1.Back To Menu")
                print("2.Exit")
                nav = int(input("Enter your option: "))
            
                if nav == 1:
                    return
                elif nav == 2:
                    print("\nExit")
                    os._exit(0)
                else:
                    print("\n Invalid option. Please try again ")
        else:
            print("\nFailed to show user information. Please try again.")
    except Exception as e:
        print("An error occured:", e)
