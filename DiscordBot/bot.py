from distutils.sysconfig import PREFIX
from msilib.schema import Component
from multiprocessing.sharedctypes import Value
import random
from sys import prefix
from tracemalloc import stop
from turtle import title
from urllib import response
import discord
from discord.ext import commands
import datetime
from discord_components import DiscordComponents, Button, ButtonStyle


# ID     1000762154976284715


client = commands.Bot( command_prefix=".", intents = discord.Intents.all())
client.remove_command("help")


#Words
hello_words = ['hello', "hi", "privet"]
info_words = ['info', 'commands', 'help']
goodbye_words = ['bye', 'good bye', "bb"]

#Connect check
@client.event
async def on_ready():
    print("Bot connected")
    
    DiscordComponents(client)
    
    await client.change_presence(activity=discord.Game(".help"))



#game
@client.command()
async def game(ctx):
    await ctx.send(
        embed = discord.Embed(title = "Coin Flip"),
        components = [
            Button(style=ButtonStyle.green, label="1"),
            Button(style=ButtonStyle.red, label="2")           
        ]
    )    
    op = ["1", "2"]
    bot_choise = random.choice(op)
    await ctx.channel.send(bot_choise)
    response = await client.wait_for("button_click")
    if response.channel == ctx.channel:
        if response.component.label == bot_choise:
            await response.respond(content = "You won!")
        else:
            await response.respond(content = "Guessed wrong!")
            

#game 2
@client.command()
async def game2(ctx):
    await ctx.send(
        embed = discord.Embed(title = "Do you want to play the game who wants to be a millionaire?"),
        components = [
            Button(style=ButtonStyle.green, label="Yes"),
            Button(style=ButtonStyle.green, label="No")           
        ]
    )  
    response = await client.wait_for("button_click")
    if response.channel == ctx.channel:
        if response.component.label == "Yes":
            await response.respond(content = "Then we start")           
        else:
            await response.respond(content = "Nobody asked you")
    
    wa = 0      #wrong answers     
    await ctx.send(
        embed = discord.Embed(title = "In the UK, the abbreviation NHS stands for National what Service?"),
        components = [
            Button(style=ButtonStyle.green, label="Health"),
            Button(style=ButtonStyle.red, label="Humanity")           
        ]
    )
    res = 0    
    response = await client.wait_for("button_click")
    if response.channel == ctx.channel:
        if response.component.label == "Health":
            res+=5000
            await response.respond(content = "Correct\n" + "your winnings are = " +  str(res) + "$")           
        else:
            wa+=1
            await response.respond(content = "correct answer - Health\n")
            
    await ctx.send(
                embed = discord.Embed(title = "Which Disney character famously leaves a glass slipper behind at a royal ball?"),
                components = [
                    Button(style=ButtonStyle.green, label="Elsa"),
                    Button(style=ButtonStyle.red, label="Cinderella")           
            ]
            )
    response = await client.wait_for("button_click")  
    if response.channel == ctx.channel:
        if response.component.label == "Cinderella":
            res+=20000
            await response.respond(content = "Correct\n" + "your winnings are = " +  str(res) + "$")
        else:
            wa+=1           
            await response.respond(content =  "correct answer - Cinderella\n")
            
    await ctx.send(
                embed = discord.Embed(title = "In 1718, which pirate died in battle off the coast of what is now North Carolina?"),
                components = [
                    Button(style=ButtonStyle.green, label="Blackbeard"),
                    Button(style=ButtonStyle.red, label="Calico Jack")           
            ]
            )
    response = await client.wait_for("button_click")  
    if response.channel == ctx.channel:
        if response.component.label == "Blackbeard":
            res+=25000
            await response.respond(content = "Correct\n" + "your winnings are = " +  str(res) + "$")
        else:
            wa+=1           
            await response.respond(content =  "correct answer - Blackbeard\n")
            
    await ctx.send(
                embed = discord.Embed(title = "In Doctor Who, what was the signature look of the fourth Doctor, as portrayed by Tom Baker?"),
                components = [
                    Button(style=ButtonStyle.green, label="Wide-brimmed hat and extra long scarf"),
                    Button(style=ButtonStyle.red, label="Bow-tie, braces and tweed jacket")           
            ]
            )
    response = await client.wait_for("button_click")  
    if response.channel == ctx.channel:
        if response.component.label == "Wide-brimmed hat and extra long scarf":
            res+=50000
            await response.respond(content = "Correct\n" + "your winnings are = " +  str(res) + "$")
        else:
            wa+=1           
            await response.respond(content =  "correct answer - Wide-brimmed hat and extra long scarf\n")
    
    await ctx.send(
                embed = discord.Embed(title = "A magnet would most likely attract which of the following?"),
                components = [
                    Button(style=ButtonStyle.green, label="Metal"),
                    Button(style=ButtonStyle.red, label="Copper")           
            ]
            )
    response = await client.wait_for("button_click")  
    if response.channel == ctx.channel:
        if response.component.label == "Metal":
            res+=150000
            await response.respond(content = "Correct\n" + "your winnings are = " +  str(res) + "$")
        else:
            wa+=1           
            await response.respond(content =  "correct answer - Metal\n")
            
    await ctx.send(
                embed = discord.Embed(title = "In what year was the first iPhone released?"),
                components = [
                    Button(style=ButtonStyle.green, label="2007"),
                    Button(style=ButtonStyle.red, label="2005")           
            ]
            )
    response = await client.wait_for("button_click")  
    if response.channel == ctx.channel:
        if response.component.label == "2007":
            res+=250000
            await response.respond(content = "Correct\n" + "your winnings are = " +  str(res) + "$")
        else:
            wa+=1          
            await response.respond(content =  "correct answer - 2007\n")
            
    await ctx.send(
                embed = discord.Embed(title = "Where did Scotch whisky originate?"),
                components = [
                    Button(style=ButtonStyle.green, label="Italy"),
                    Button(style=ButtonStyle.red, label="Scotland")           
            ]
            )
    response = await client.wait_for("button_click")  
    if response.channel == ctx.channel:
        if response.component.label == "Scotland":
            res+=500000
            await response.respond(content = "Correct\n" + "your winnings are = " +  str(res) + "$")
        else:
            wa+=1           
            await response.respond(content =  "correct answer - Scotland\n")
        
    if wa >= 2:
        res = int(res)/2   
    await ctx.send(
                embed = discord.Embed(title = "your winnings is " + str(res) + "$")
            )
        








#Clear message   
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount = 100):
    await ctx.channel.purge(limit = amount)
    
#kick
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge(limit = 1)
    await member.kick(reason=reason)
    
    
#mute   
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)    
async def mute(ctx, member: discord.Member):
    await ctx.channel.purge(limit = 1)
    mute = discord.utils.get(ctx.message.guild.roles, name = "mute")
    await member.add_roles(mute)
    await ctx.send(f"{member.mention} muted")
    
    
 
#Ban
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge(limit = 1)
    await member.ban(reason=reason)
#Unban
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    await ctx.channel.purge(limit = 1)   
    banned_users = await ctx.guild.bans()    
    for ban_entry in banned_users:
        user = ban_entry.user       
        await ctx.guild.unban(user)
        await ctx.send(f"Unbanned user {user.mention}")        
        return

 
#Meme 
@client.command()
async def meme(ctx):
     
    rand_num = random.randint(1,15)
    if rand_num == 1:
        emb = discord.Embed(title = "meme", colour=discord.Colour.dark_green())
        emb.set_image(url = "https://i.imgur.com/Hab3RJO.jpg")
    if rand_num == 2:
        emb = discord.Embed(title = "meme", colour=discord.Colour.dark_green())
        emb.set_image(url = "https://i.imgur.com/tWPf0go.jpeg")
    if rand_num == 3:
        emb = discord.Embed(title = "meme", colour=discord.Colour.dark_green())
        emb.set_image(url = "https://i.imgur.com/IL02dqN.jpeg")
    if rand_num == 4:
        emb = discord.Embed(title = "meme", colour=discord.Colour.dark_green())
        emb.set_image(url = "https://i.imgur.com/sFstzed.jpeg")
    if  rand_num == 5: 
        emb = discord.Embed(title = "meme", colour=discord.Colour.dark_green())
        emb.set_image(url = "https://i.imgur.com/CuSuXRi.png") 
    if  rand_num == 6:
        emb = discord.Embed(title = "meme", colour=discord.Colour.dark_green())
        emb.set_image(url = "https://i.imgur.com/qaol2ux.jpeg")
    if  rand_num == 7:
        emb = discord.Embed(title = "meme", colour=discord.Colour.dark_green())
        emb.set_image(url = "https://i.imgur.com/u8Fy82t.jpeg")
    if  rand_num == 8:
        emb = discord.Embed(title = "meme", colour=discord.Colour.dark_green())
        emb.set_image(url = "https://i.imgur.com/ygiYI7Q.jpeg")
    if  rand_num == 9:
        emb = discord.Embed(title = "meme", colour=discord.Colour.dark_green())
        emb.set_image(url = "https://i.imgur.com/YfX7fAx.jpeg")
    if  rand_num == 10:
        emb = discord.Embed(title = "meme", colour=discord.Colour.dark_green())
        emb.set_image(url = "https://i.imgur.com/IAeXiUL.jpeg")
    if  rand_num == 11:
        emb = discord.Embed(title = "meme", colour=discord.Colour.dark_green())
        emb.set_image(url = "https://i.imgur.com/yDtpahp.jpeg")
    if  rand_num == 12:
        emb = discord.Embed(title = "meme", colour=discord.Colour.dark_green())
        emb.set_image(url = "https://i.imgur.com/RW3A6CX.jpeg")
    if  rand_num == 13:
        emb = discord.Embed(title = "meme", colour=discord.Colour.dark_green())
        emb.set_image(url = "https://i.imgur.com/WmoZv9F.jpeg")
    if  rand_num == 14:
        emb = discord.Embed(title = "meme", colour=discord.Colour.dark_green())
        emb.set_image(url = "https://i.imgur.com/tydQWp0.jpeg")
    if  rand_num == 15:
        emb = discord.Embed(title = "meme", colour=discord.Colour.dark_green())
        emb.set_image(url = "https://i.imgur.com/6xDAVai.jpeg")
    
    await ctx.send(embed = emb)





#Help
@client.command(pass_context = True)
async def help(ctx):
    await ctx.channel.purge(limit = 1)
    emb = discord.Embed(title = "Navigation")
    
    emb.add_field(name = ".ban", value="ban users(Admin)")
    emb.add_field(name = ".unban", value="Unban users(Admin)")
    emb.add_field(name = ".mute", value="mute(Admin)")
    emb.add_field(name = ".kick", value="kick users(Admin)")
    emb.add_field(name = ".clear", value="clear chat(Admin)")
    emb.add_field(name = ".time", value="Time")
    emb.add_field(name = ".meme", value="Meme")
    emb.add_field(name = ".game", value="Coin Flip")
    emb.add_field(name = ".game2", value="Who wants to be a millionaire?")
    
    
    await ctx.send( embed = emb )


#time
@client.command(pass_context = True)

async def time(ctx):
    await ctx.channel.purge(limit = 1)
    emb = discord.Embed(title = "Time", colour = discord.Color.red(), url = "https://time.is/bg/") 
    date = datetime.datetime.now()   
    emb.add_field(name = "Time", value="{}".format(date))   
    await ctx.send(embed = emb)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content.lower()
    
    if msg in hello_words:
        hello_answers = ["Hello, how are you?", "Hello", "Hi", "Long time no see!", "Look, who's here!", "It is so nice to see you again",
                         "Nice to meet you"]
        await message.channel.send(random.choice(hello_answers))
        
    if msg in info_words:
        await message.channel.send("use command .help")
    
    if msg in goodbye_words:
        goodbye_answers = ["Good Bye my friend", "Take care", "Bye", "Bye for now", "See you soon", "See ya!", 
                           "See you later", "GoodBye!", "Have a good one"]
        await message.channel.send(random.choice(goodbye_answers))
    await client.process_commands(message)    
    




#Token
token = open('token.txt.txt', 'r').readline()

client.run( token )





