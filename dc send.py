import requests
#input data
token = input("Token : ")
channel_id = input("Channel ID : ")
message = input("Message : ")
#parse data
url_send = f"https://discord.com/api/v9/channels/{channel_id}/messages"
payload = {"content" : f"{message}"}
headers = {"Authorization": f"{token}"}
#send request
res = requests.post(url_send, payload, headers=headers)
