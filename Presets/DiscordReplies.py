import discord
from Requirements.DiscordConfig import settings


class Post:
    def createEmbed(image_board, cens_type, post, post_rating):
        source = {'dan': 'Danbooru', 'gel': 'Gelbooru', 'none': 'Неизвестный источник'}
        censor = {'safe': 'С цензурой', 'nsfw': 'Без цензуры', 'none': ':snake:'}
        color = {'safe': settings['embed_color1'], 'nsfw': settings['embed_color2']}

        def text_editor(text):  # Форматирование тегов
            text = text.replace(" ", ", ")
            text = text.replace("_", " ")
            text = text.title()
            return text

        embed = discord.Embed(title=f"Пикча получена с {source[image_board]}", description=f"{censor[cens_type]}",
                              color=color[cens_type])
        embed.add_field(name="Автор", value=f"{text_editor(post['author'])}", inline=False)
        embed.add_field(name="Теги", value=f"Персонаж: {text_editor(post['character'])}\n"
                                           f"Копирайт: {text_editor(post['copyright'])}")
        embed.add_field(name="Линк", value=f"https://danbooru.donmai.us/posts/{post['post_id']}", inline=False)
        embed.set_image(url=post['file_url'])
        embed.set_footer(text=f"Рейтинг пикчи: {post_rating}\n")
        return embed

    def helpList(self):
        embed = discord.Embed(title="Список команд бота")
        embed.add_field(name="!d", value="*Реквест пикчи с Danbooru + 1 тег (с цензурой)*", inline=False)
        embed.add_field(name="!du", value="*Реквест пикчи с Danbooru + 1 тег (без цензуры)*", inline=False)
        embed.add_field(name="!g", value="*Реквест пикчи с Gelbooru + неограниченное кол-во тегов*\n"
                                           "(:wrench: *Пока не доработанно* :wrench:)")
        embed.set_footer(text="Автор бота - asdo")
        return embed
