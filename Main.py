import discord
import pybooru
import pygelbooru
from Presets.DiscordReplies import Post
from Requirements.DiscordConfig import settings
from Importers.ImportDan import Req_pic
from discord.ext import commands
from Presets.Censor import Censor


intents = discord.Intents.all()
bot = commands.Bot(command_prefix = (settings['prefix']), intents = intents)
user = discord.user
bot.remove_command('help')


@bot.command()
async def help(ctx):
    help_list = Post.helpList(None)
    await ctx.send (embed = help_list)


@bot.command()
async def dan(ctx): # Реквест пикчи с данбору с цензурой
    author = ctx.message.author

    try:
        content = ctx.message.content.replace('!dan', '')
        post = Req_pic.danpic(content)
        print(f"Рейтинг пикчи: {post['rating']}")

        if post['rating'] == 'e' or post['rating'] == 'q':
            post = Censor.censorDef(post, content)

        await ctx.send(embed = Post.createEmbed('dan', 'safe', post, Censor.rating(post)))

    except IndexError:
        await ctx.send(f"{author.mention}, введённого тега не существует, попробуй что-то другое")
    except pybooru.exceptions.PybooruHTTPError:
        await ctx.send(f"{author.mention}, нельзя запросить больше двух тегов!")
    except KeyError:
        await ctx.send(f"{author.mention}, этот тег заблокирован, либо в посте отсутствует пикча.")
    except TypeError:
        await ctx.send(f"{author.mention}, параметр к тегу задан неверно, либо другая ошибка.")
    except Exception as e:
        print(e)


@bot.command()
async def danun(ctx): # Реквест пикчи с данбору без цензуры
    author = ctx.message.author

    try:
        content = ctx.message.content.replace('!danun', '')

        post = Req_pic.danpic(content)
        print(f"Рейтинг пикчи: {post['rating']}")

        await ctx.send(embed = Post.createEmbed('dan', 'nsfw', post, Censor.rating(post)))
        
    except IndexError:
        await ctx.send(f"{author.mention}, введённого тега не существует, попробуй что-то другое")
    except pybooru.exceptions.PybooruHTTPError:
        await ctx.send(f"{author.mention}, нельзя запросить больше двух тегов!")
    except KeyError:
        await ctx.send(f"{author.mention}, этот тег заблокирован, либо в посте отсутствует пикча.")
    except TypeError:
        await ctx.send(f"{author.mention}, параметр к тегу задан неверно, либо другая ошибка.")
    except Exception as e:
        print(e)


@bot.command()
async def gel(ctx): # Реквест пикчи с гелбуру

    await ctx.send(":wrench: WIP :wrench:")

bot.run(settings['token'])
