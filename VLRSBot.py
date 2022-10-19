from pydoc import describe
import discord
from discord.ext import commands
import psycopg2
import tracemalloc

#tracemalloc.start()


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="/", intents = intents, case_insensitive = True)
bot = discord.Bot()

SERVER = #removed it to make the code public
TOKEN = #removed it to make the code public

DB_HOST = 'localhost'
DB_NAME = #removed it to make the code public
DB_USER = 'postgres'
DB_PASS = #removed it to make the code public
DB_PORT = 5432

VALOROUS_COIN='<:valorous_coin:942020599721631784>'

DICT = {"Pic perm": 3, "Novice": 5, "Intermediate": 10, "Advanced" : 20}


"""
@bot.slash_command(name='createdb',guild_ids=[SERVER])
@commands.is_owner()
async def createdb(ctx):
    moneydb = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT)
    cur = moneydb.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS MONEY (userid BIGINT PRIMARY KEY, guildid BIGINT, balance INT);")
    moneydb.commit()
    cur.close()
    moneydb.close()
    await ctx.respond(content = "Setup complete")
"""



@bot.slash_command(name='register', description='Registers selected user in the bot!', guild_ids=[SERVER])
async def register (ctx, member : discord.Member):
    moneydb = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT)
    cur = moneydb.cursor()
    SQL = """SELECT userid FROM MONEY WHERE userid = %s"""
    cur.execute(SQL,(member.id,))
    test = cur.fetchone()
    booltest = test is None
    if booltest == True:
        cur.execute("""INSERT INTO MONEY (userid,guildid,balance) VALUES (%s,%s,%s)""", (int(member.id),int(ctx.guild.id),0))
        moneydb.commit()
        await ctx.respond(content = "You are now registered!")
    else:
        await ctx.respond(content = "You were already registered!")
    cur.close()
    moneydb.close()


@bot.slash_command(name='addcoins', description='Adds coins to selected user!', guild_ids=[SERVER])
@commands.has_role('vlrsbotperm')
async def addcoins (ctx, member : discord.Member, newcoins : int):
    moneydb = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT)
    cur = moneydb.cursor()
    SQL = """UPDATE MONEY SET balance = balance + %s WHERE userid = %s"""
    cur.execute(SQL,(int(newcoins),int(member.id)))
    moneydb.commit()
    await ctx.respond(content ="Done")
    print(member.id, member.name, "received", newcoins, "coins")
    
async def howmanycoins(ctx, member : discord.Member):
    moneydb = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT)
    cur = moneydb.cursor()
    SQL = "SELECT balance FROM MONEY WHERE userid = %s"
    cur.execute(SQL,(member.id,))
    bal = cur.fetchone()
    
    bal = str(bal)
    bal = bal.replace("(", "")
    bal = bal.replace(")", "")
    bal = bal.replace(",", "")
    return bal

@bot.slash_command(name='coins', description='Shows how many coins selected user has', guild_ids=[SERVER])
async def coins(ctx, member : discord.Member):
    embed = discord.Embed()
    bal = await howmanycoins(ctx, member)
    embed.add_field(name="Balance : ", value=f" {member.name} has {bal} {VALOROUS_COIN}")
    await ctx.respond(embed=embed)


@bot.slash_command(name='shop', description='Displays what items are available in the shop', guild_ids=[SERVER])
async def shop(ctx):
    embed = discord.Embed()
    embed.add_field(name="Shop : ", value=f"Pic perm : 3 {VALOROUS_COIN} \nNovice : 5 {VALOROUS_COIN} \nIntermediate : 10 {VALOROUS_COIN} \nAdvanced : 20 {VALOROUS_COIN}")
    await ctx.respond(embed=embed)


@bot.slash_command(name='buy', description='Allows user to buy items', guild_ids=[SERVER])
async def buy(ctx, item : str):
    member = ctx.author
    bal = await howmanycoins(ctx, member)
    bal = int(bal)
    if item in DICT.keys():
        if bal >= 5:
            role = discord.utils.get(ctx.guild.roles, name=item)
            if role in member.roles:
                await ctx.respond(content="You already have this role.")
            else:
                await member.add_roles(role)
                await addcoins (ctx, member,-DICT[item])
                await ctx.respond(content="You have received your role! ")
                print(member.id,member.name,"bought",item)
        else:
            await ctx.respond(content="You do not have enough Valorous coins to purchase this item.")
    else:
        await ctx.respond(content="You did not enter a valid item. ")



@bot.slash_command(name='leaderboard', description='Shows the list of the top 5 users who have the most coins.', guild_ids=[SERVER])
async def leaderboard(ctx):
    moneydb = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT)
    cur = moneydb.cursor()
    cur.execute("SELECT userid, balance FROM MONEY ORDER BY balance DESC LIMIT 5")
    lb = cur.fetchall()
    embed = discord.Embed()
    i = 0
    for row in lb:
        raw_id = int(row[0])
        member = await bot.fetch_user(raw_id)
        x = ("{},  {}".format(member.mention, row[1]))
        i += 1
        embed.add_field(name=f"Top {i}", value = f"{x} {VALOROUS_COIN}", inline=False)
    await ctx.respond(embed=embed)
    

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Subscribe to Valorous Gaming on Youtube!'))
    print("The bot is online")
    
"""    
@bot.event
async def on_message(ctx,self,message):
    user_message = str(message.content)
    if message.author == self.author:
        return
    elif user_message.lower() == 'alpha':
        await ctx.send("Flower")
        return
    elif user_message.lower() == 'glow':
        await ctx.send("Dog")
        return
"""   

bot.run(TOKEN)