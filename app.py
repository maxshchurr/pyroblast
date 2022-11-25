from pyrogram import Client
import cohere

"""
So to start with Pyrogram we have to make some manipulations.
1 step - visit https://my.telegram.org/auth and login with your phone number.
2 step - after successful authentication you will be redirected to a page. 
There you'll find App api_id and App api_hash.These fields are used below (api_id and api_hash).
We will need them only once for the first running.
To run script we use this line:app = Client("pyroApp", api_id=api_id, api_hash=api_hash)

More about Pyrogram: https://docs.pyrogram.org/
More about cohere: https://docs.cohere.ai/docs
"""

# api_id = your api_id
#
# api_hash = "your api_hash"
#
# app = Client("pyroApp", api_id=api_id, api_hash=api_hash)

group = "me"
app = Client("pyroApp")
all_msg = ['hello', 'hii']
with app:
    for message in app.get_chat_history(group):
        if message.text is not None:
            all_msg.append(message.text)


co = cohere.Client('R3ZspcOxRQuTMdS5i0UPR2Ozo0shjRmUAEsOoFoe')

response = co.embed(
    model='small',
    texts=all_msg
)

print(response)

# app.run()