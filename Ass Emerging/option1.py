import requests, os

def connectData(tokenData):
    try:
        url = 'https://webexapis.com/v1/people/me'
        headers = {
            'Authorization' : 'Bearer {}'.format(tokenData)
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print("\nFailed to connect to Webex server. Please try again.")
        else:
            print("\n Successfully Connected to Webex Server! ")
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
                    print("\n Invalid option.Please try again ")

    except Exception as e:
        print("An error occurred:", e)
