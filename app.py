from pyrogram import Client
"""
So to start with Pyrogram we have to make some manipulations.
1 step - visit https://my.telegram.org/auth and login with your phone number.
2 step - after successful authentication you will be redirected to a page. 
There you'll find App api_id and App api_hash.These fields are used below (api_id and api_hash).
We will need them only once for the first running.
To run script we use this line:app = Client("pyroApp", api_id=api_id, api_hash=api_hash)
"""

# api_id = your api_id
#
# api_hash = "your api_hash"
#
# app = Client("pyroApp", api_id=api_id, api_hash=api_hash)

group = "me"
app = Client("pyroApp")
all_msg = []
with app:
    for message in app.get_chat_history(group):

        all_msg.append(message.text)


print(all_msg)
# app.run()