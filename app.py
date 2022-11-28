from pyrogram import Client
import cohere
import weaviate # to communicate to the Weaviate instance

"""
So to start with Pyrogram we have to make some manipulations.
Visit https://my.telegram.org/auth and login with your phone number.
After successful authentication you will be redirected to a page. 
There you'll find App api_id and App api_hash.These fields are used below (api_id and api_hash).
We will need them only once for the first running.
To run script we use this line:app = Client("pyroApp", api_id=api_id, api_hash=api_hash)

More about Pyrogram: https://docs.pyrogram.org/
More about cohere: https://docs.cohere.ai/docs
More about weaviate: https://weaviate.io/
"""

"""
Step 1

api_id = 23434761
api_hash = "58349ea9b93ba4235f632a706fe149bc"

app = Client("my_account", api_id=api_id, api_hash=api_hash)

app.run()


Step 2

Sign In https://console.semi.technology/ and create a Weaviate Cluster
Connect to this cluster from web


Step 3 

Here is cluster's name that you have change to yours  
in models.py
client = weaviate.Client("https://your_cluster.semi.network")

and in app.py
client_url = "https://your_cluster.semi.network"

Then run models.py to create classes


Step 4 

If you want to use cohere visit this site https://docs.cohere.ai/reference/embed and copy authentication string 

co = cohere.Client('your_auth')

Step 5

Run app.py

Step 6

Visit https://console.semi.technology/console/query

You'll see your schema and query tool
To get extracted data run this in query tool

 {
  Get{
    Posts{
      description
    }
  }
}

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
group = "me"
data = get_posts_from_the_channel(group)


# Turn into embeddings with cohere
embeddings = turn_into_embeddings(data)


# Adding channel and retrieved posts from the channel to db
client_url = "https://test1.semi.network"

add_posts(embeddings, client_url)
# add_channel(group, client_url)












