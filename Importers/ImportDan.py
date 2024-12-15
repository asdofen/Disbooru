from pybooru import Danbooru
from Requirements import danbooru_api_info


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