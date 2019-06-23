import os
import typetalk

bot = typetalk.Bot(token=os.environ['TYPETALK_TOKEN'])

res = bot.post_message(
    topic_id=os.environ['TYPETALK_TOPIC_ID'],
    message='Hello, world!'
)
assert res['post']['message'] == 'Hello, world!'
