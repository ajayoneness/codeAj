import requests
import json

url = "https://www.fast2sms.com/dev/bulk"

# create a dictionary
my_data = {
    # Your default Sender ID
    'sender_id': 'TXTIND',

    # Put your message here!
    'message': 'This is a test message',

    'language': 'english',
    'route': 'P',

    # You can send sms to multiple numbers
    # separated by comma.
    'numbers': '8603862290, 7464034854, 8578829260'
}

# create a dictionary
headers = {
    'authorization': 'oLdsZvs9M2S4F6jnSFbvQxc8BczzHxP386dWFJdwehjIjvdozIAj32OnYAui',
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache"
}

# make a post request
response = requests.request("POST",
                            url,
                            data=my_data,
                            headers=headers)
#load json data from source

returned_msg = json.loads(response.text)

# print the send message
print(returned_msg['message'])