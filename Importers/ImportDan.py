from pybooru import Danbooru
from pygelbooru import Gelbooru
from Requirements.DanbooruKeys import danbooru_api_info
from Requirements.GelbooruKeys import gelbooru_api_info
import asyncio


class Req_pic:
    def __init__(self):
        print('init')

    def danpic(tags):
        username = (danbooru_api_info['login'])
        api_key = (danbooru_api_info['key'])    
            
        dan = Danbooru('danbooru', username=username, api_key=api_key)
        posts = dan.post_list(tags=tags, limit=1, random="True")
        print (posts)
        post = {
            'author': posts[0]['tag_string_artist'],
            'file_url': posts[0]['file_url'],
            'rating': posts[0]['rating'],
            'copyright': posts[0]['tag_string_copyright'],
            'character': posts[0]['tag_string_character'],
            'tags': posts[0]['tag_string_general'],
            'post_id': posts[0]['id']
        }
        
        return post
    

    async def gelpicrand(tags):
        username = (gelbooru_api_info['login'])
        api_key = (gelbooru_api_info['key'])

        gel = Gelbooru(api_key=api_key, user_id=username)
        posts = await gel.random_post(tags=tags.split())
        cooltags = await gel.tag_list(name_pattern=posts.tags)
        print (cooltags)

        """"
        post = {
            'author': posts[0]['tag_string_artist'],
            'file_url': posts[0]['file_url'],
            'rating': posts[0]['rating'],
            'copyright': posts[0]['tag_string_copyright']
            'tags': posts.tags,
            'post_link': posts.id
        }
        """
        return posts


# Gelbooru wrapper tester
"""
user=input(str())

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(Req_pic.gelpicrand(user))
"""