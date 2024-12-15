import discord
import pybooru
from Presets.DiscordReplies import Post
from Requirements import dis_settings
from Importers.ImportDan import Req_pic
from discord.ext import commands
from Presets.Censor import Censor


intents = discord.Intents.all()
bot = commands.Bot(command_prefix = (dis_settings['prefix']), intents = intents)
user = discord.user
bot.remove_command('help')


@bot.command()
async def help(ctx):
    help_list = Post.helpList(None)
    await ctx.send (embed = help_list)


@bot.command()
async def dan(ctx): # Danbooru request censored
    author = ctx.message.author

    try:
        content = ctx.message.content.replace('!dan', '')
        post = Req_pic.danpic(content)
        print(f"Rating: {post['rating']}")

        if post['rating'] == 'e' or post['rating'] == 'q':
            post = Censor.censorDef(post, content)

        await ctx.send(embed = Post.createEmbed('dan', 'safe', post, Censor.rating(post)))

    except IndexError:
        await ctx.send(f"{author.mention}, Nobody here but us chickens! Maybe entered tag doesn't exist.")
    except pybooru.exceptions.PybooruHTTPError:
        await ctx.send(f"{author.mention}, You cannot search for more than 2 tags at a time.")
    except KeyError:
        await ctx.send(f"{author.mention}, Blacklisted tag or post does not contains image.")
    except TypeError:
        await ctx.send(f"{author.mention}, Unknown error.")
    except Exception as e:
        print(e)


@bot.command()
async def danun(ctx): # Danbooru request uncensored
    author = ctx.message.author

    try:
        content = ctx.message.content.replace('!danun', '')

        post = Req_pic.danpic(content)
        print(f"Рейтинг пикчи: {post['rating']}")

        await ctx.send(embed = Post.createEmbed('dan', 'nsfw', post, Censor.rating(post)))
        
    except IndexError:
        await ctx.send(f"{author.mention}, Nobody here but us chickens! Maybe entered tag doesn't exist.")
    except pybooru.exceptions.PybooruHTTPError:
        await ctx.send(f"{author.mention}, You cannot search for more than 2 tags at a time.")
    except KeyError:
        await ctx.send(f"{author.mention}, Blacklisted tag or post does not contains image.")
    except TypeError:
        await ctx.send(f"{author.mention}, Unknown error.")
    except Exception as e:
        print(e)


@bot.command()
async def gel(ctx): # Gelbooru request

    await ctx.send(":wrench: WIP :wrench:")

bot.run(dis_settings['token'])
