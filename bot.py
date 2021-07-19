# bot.py

import os
import asyncio
import random
import winsound
import time

from twitchio.ext import commands

bot = commands.Bot(
    # setting up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    api_token=os.environ['API_TOKEN'],
    initial_channels=[os.environ['CHANNEL']],
    user_id=[os.environ['USER_ID']]
    )

timer = time.time()

@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws
    if os.path.exists("C:/Users/Bryson Hayes/Documents/Twitch Bot/stream/counter.txt"):
        os.remove("C:/Users/Bryson Hayes/Documents/Twitch Bot/stream/counter.txt")
    file_path = 'C:/Users/Bryson Hayes/Documents/Twitch Bot/stream/counter.txt'
    file = open(file_path, "w")
    file.write("0")
    file.close()
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has strut his stuff into the stream. Everyone get down and put your hands up! murdoiNk")
    
def counter():
    global count
    file_path = 'C:/Users/Bryson Hayes/Documents/Twitch Bot/stream/counter.txt'
    file = open(file_path, "r")
    count = int(file.read())
    file.close()
    count += 1
    file = open(file_path, "w")
    count = str(count)
    file.write(count)
    file.close()
    return count

def cd(timer):  
    global elapsed
    current_time = time.time()
    elapsed = int(current_time - timer)
    return elapsed
    
@bot.event
async def event_message(ctx):
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return
    else:
        message = ctx.content.split(' ')[0:]
        ws = bot._ws
        if 'atpTryAiming' in message:
            await ws.send_privmsg(os.environ['CHANNEL'],f'atpTryAiming')
    await bot.handle_commands(ctx)

@bot.command(name='shoot')
async def shoot(ctx):
    option = random.randrange(6)
    mods = ["bhvithai", "@bhvithai", "d4nk_d4ddy", "@d4nk_d4ddy", "tryaimingbot", "@tryaimingbot"]
    try:
        name = ctx.content.split(' ')[1]
        if ctx.author.is_mod == 1:
            if option == 0 or option == 1 or option == 2:
                winsound.PlaySound("C:/Users/Bryson Hayes/Documents/Twitch Bot/sounds/book.wav",winsound.SND_ASYNC)
                await ctx.timeout(name,10,"Yes sir!")
                await ctx.send(f"Book 'em boys. atpBelligerent")
                counter()
                await ctx.send(f"{count} users have been shot in chat today. Why always the fighting? atpCrab")
            else:
                winsound.PlaySound("C:/Users/Bryson Hayes/Documents/Twitch Bot/sounds/arrest.wav",winsound.SND_ASYNC)
                await ctx.send(f"I've got everything I need to convict you {name} except for motive, means and opportunity. atpCheif")
        elif ctx.author.name == 'thatjohndenver':
            winsound.PlaySound("C:/Users/Bryson Hayes/Documents/Twitch Bot/sounds/meow.wav",winsound.SND_ASYNC)
            await ctx.send(f'InuyoFace GlitchCat DxCat')
        else:
            winsound.PlaySound("C:/Users/Bryson Hayes/Documents/Twitch Bot/sounds/bang.wav",winsound.SND_ASYNC)
            for x in mods:
                if name == x:
                    await ctx.timeout(ctx.author.name,600,f"Don't shoot the mods kid.")
                    await ctx.send(f"Let that be a lesson to you all atpCornteen")
                    counter()
                    await ctx.send(f"{count} users have been shot in chat today. Why always the fighting? atpCrab")
                break
            if name == 'thatjohndenver' or name == '@thatjohndenver':
                await ctx.timeout(ctx.author.name,1,f"Don't shoot TJD")
                await ctx.send(f"The Cat Lady must be protected at all costs! atpLook")
            else:
                if option == 0:
                    await ctx.timeout(name,10,f"At your service")
                    await ctx.send(f'{ctx.author.name} shot {name}. Nice shot atpQuan')
                    counter()
                    await ctx.send(f"{count} users have been shot in chat today. Why always the fighting? atpCrab")
                elif option == 1:
                    await ctx.timeout(ctx.author.name,10,f"Nice try sucka")
                    await ctx.send(f'{ctx.author.name} shot themselves in the foot atpDisorderly')
                    counter()
                    await ctx.send(f"{count} users have been shot in chat today. Why always the fighting? atpCrab")
                elif option == 2:
                    await ctx.timeout('rebovast',10,f"None needed")
                    await ctx.timeout(name,10,f"Headshot")
                    await ctx.timeout(ctx.author.name,10,f"Bouncy bullets")
                    await ctx.send(f'{ctx.author.name} and {name} exchanged shots, and rebovast was hit with a stray bullet atpTryAiming')
                    for _ in range(3):
                        counter()
                    await ctx.send(f"{count} users have been shot in chat today. Why always the fighting? atpCrab")
                elif option == 3:
                    winsound.PlaySound("C:/Users/Bryson Hayes/Documents/Twitch Bot/sounds/gunshot2.wav",winsound.SND_ASYNC)
                    await ctx.timeout(ctx.author.name,77,f"7 7 7")
                    await ctx.send(f'{ctx.author.name} played Russian Roulette and lost. atp7 atp7 atp7')
                    counter()
                    await ctx.send(f"{count} users have been shot in chat today. Why always the fighting? atpCrab")
                elif option == 4:
                    await ctx.timeout(ctx.author.name,30,f"Way to go")
                    await ctx.send(f'{ctx.author.name} blew off a limb. It will grow back. atpCap')
                    counter()
                    await ctx.send(f"{count} users have been shot in chat today. Why always the fighting? atpCrab")
                elif option ==5:
                    await ctx.send(f'{ctx.author.name} tried to shoot {name} but drew a blank. Better watch out atpNinja')
    except IndexError:
        await ctx.send('Please identify your target. atpCop')

@bot.command(name='panda')
async def panda(ctx):
    winsound.PlaySound("C:/Users/Bryson Hayes/Documents/Twitch Bot/sounds/panda.wav",winsound.SND_ASYNC)
    await ctx.send(f'atpHarada')

@bot.command(name='sand')
async def sand(ctx):
    winsound.PlaySound("C:/Users/Bryson Hayes/Documents/Twitch Bot/sounds/sand.wav",winsound.SND_ASYNC)

@bot.command(name='dog')
async def dog(ctx):
    winsound.PlaySound("C:/Users/Bryson Hayes/Documents/Twitch Bot/sounds/dog.wav",winsound.SND_ASYNC)

@bot.command(name='wrongway')
async def wrongway(ctx):
    winsound.PlaySound("C:/Users/Bryson Hayes/Documents/Twitch Bot/sounds/wrongway.wav",winsound.SND_ASYNC)

@bot.command(name='clip')
async def clip(ctx):
    global timer
    cd(timer)
    if elapsed > 60:
        clip = await bot.create_clip(os.environ["API_TOKEN"],os.environ['USER_ID'])
        clip_url = clip[0]['id']
        await ctx.send(f"Thanks for the clip! https://www.twitch.tv/bhvithai/clip/{clip_url}")
        timer = time.time()
    else:
        cooldown = 60 - elapsed
        await ctx.send(f"Bot is on cooldown, try again in {cooldown} seconds")

@bot.command(name='help')
async def help(ctx):
    await ctx.send(f'TryAimingBot is a chatbot programmed in Python using TwitchIO. Try one of the !commands in chat.')
    
@bot.command(name='commands')
async def commands(ctx):
    await ctx.send(f'The following commands are available in chat: !help !shoot !clip !panda !sand !dog !wrongway')

if __name__ == "__main__":
    bot.run()
