from pyrogram import Client
import cohere
import weaviate # to communicate to the Weaviate instance
from weaviate.wcs import WCS


"""
So to start with Pyrogram we have to make some manipulations.
1 step - visit https://my.telegram.org/auth and login with your phone number.
2 step - after successful authentication you will be redirected to a page. 
There you'll find App api_id and App api_hash.These fields are used below (api_id and api_hash).
We will need them only once for the first running.
To run script we use this line:app = Client("pyroApp", api_id=api_id, api_hash=api_hash)

More about Pyrogram: https://docs.pyrogram.org/
More about cohere: https://docs.cohere.ai/docs
More about weaviate: https://weaviate.io/
"""

# api_id = your api_id

# api_hash = "your api_hash"

# app = Client("pyroApp", api_id=api_id, api_hash=api_hash)


def turn_into_embeddings(data):
    co = cohere.Client('R3ZspcOxRQuTMdS5i0UPR2Ozo0shjRmUAEsOoFoe')

    response = co.embed(
        model='small',
        texts=data
    )

    return response


def get_posts_from_the_channel(group_id):
    channel = group_id
    app = Client("pyroApp")
    all_msg = []
    with app:
        for message in app.get_chat_history(channel):
            if message.text is not None:
                all_msg.append(message.text)

    return all_msg


def add_channel(channel, db_url):
    client = weaviate.Client(db_url)
    properties = {"name": channel}
    client.batch.add_data_object(properties, "Channels")

    client.batch.create_objects()


def add_posts(data, db_url):
    client = weaviate.Client(db_url)

    for msg in data:
        properties = {
          "description": msg
        }

        client.batch.add_data_object(properties, "Posts")

    client.batch.create_objects()


# Defining the group and retrieving posts from the group
group = "MargulanSeissembai"
data = get_posts_from_the_channel(group)


# Turn into embeddings with cohere
embeddings = turn_into_embeddings(data)


# Adding channel and retrieved posts from the channel to db
client_url = "https://test1.semi.network"

add_posts(embeddings, client_url)
# add_channel(group, client_url)












