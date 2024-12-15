from Importers.ImportDan import Req_pic


class Censor:
    def rating(post):
        if post['rating'] == 's' or post['rating'] == 'g':
            post_rating = "Safe"
        elif post['rating'] == 'q' or post['rating'] == 'e':
            post_rating = "Explicit"
        return post_rating

    def censorDef(post, content):
        for i in range(3):
            if post['rating'] == 'e' or post['rating'] == 'q':
                post = Req_pic.danpic(content)
                print(f"Rating: {post['rating']}")
                if post['rating'] == 'g' or post['rating'] == 's':
                    return post
                else:
                    post['file_url'] = 'https://media.tenor.com/0LtvGK3-jb0AAAAM/anime-no.gif'
                    return post
                continue
