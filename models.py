import weaviate


class_channel_obj = {
  "class": "Channels",
  "description": "A channel from telegram",
  "properties": [
    {
      "dataType": [
        "string"
      ],
      "description": "Name of the channel",
      "name": "name"
    },
    {
        "name": "PostsFromTheChannel",
        "dataType": ["Posts"],
        "description": "The posts from the channel",
    }
  ]
}


class_post_obj = {
  "class": "Posts",
  "description": "Posts from the channel",
  "properties": [
        {
            "name": "Posts",
            "dataType": ["string"],
            "description": "Post content",
        }
    ]

}

# Not sure about this

# reference_property = {
#   "dataType": [
#     "Posts"
#   ],
#   "description": "The posts this channel has",
#   "name": "hasPosts"
# }


client = weaviate.Client("https://test1.semi.network")


client.schema.create_class(class_post_obj)
client.schema.create_class(class_channel_obj)

# client.schema.delete_class('Channels')
# client.schema.delete_class('Posts')

# client.schema.property.create("Channels", reference_property)