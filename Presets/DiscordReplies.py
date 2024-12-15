import discord
from Requirements import dis_settings


class Post:
    def createEmbed(image_board, cens_type, post, post_rating):
        source = {'dan': 'Danbooru', 'gel': 'Gelbooru', 'none': 'Unexpected archive'}
        censor = {'safe': 'Censored', 'nsfw': 'Uncensored', 'none': ':snake:'}
        color = {'safe': dis_settings['embed_color1'], 'nsfw': dis_settings['embed_color2']}

        def text_editor(text):  # Tag formating
            text = text.replace(" ", ", ")
            text = text.replace("_", " ")
            text = text.title()
            return text

        embed = discord.Embed(title=f"Image source archive {source[image_board]}", description=f"{censor[cens_type]}",
                              color=color[cens_type])
        embed.add_field(name="Author", value=f"{text_editor(post['author'])}", inline=False)
        embed.add_field(name="Tags", value=f"Character: {text_editor(post['character'])}\n"
                                           f"Copyright: {text_editor(post['copyright'])}")
        embed.add_field(name="Source", value=f"https://danbooru.donmai.us/posts/{post['post_id']}", inline=False)
        embed.set_image(url=post['file_url'])
        embed.set_footer(text=f"Rating: {post_rating}\n")
        return embed

    def helpList(self):
        embed = discord.Embed(title="Command list:")
        embed.add_field(name="!dan", value="*Request random picture from Danbooru (censored) +1 extra tag*", inline=False)
        embed.add_field(name="!danun", value="*Request random picture from Danbooru (uncensored) +1 extra tag*", inline=False)
        embed.add_field(name="!gel", value="*Request random picture from Gelbooru*\n"
                                           "(:wrench: *Wordk in progress* :wrench:)")
        embed.set_footer(text="Powered by Disbooru")
        return embed
