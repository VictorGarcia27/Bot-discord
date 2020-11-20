from discord.ext import commands
import random
import os
import discord
import typing

client = discord.Client()
commandPrefix = "!"
bot = commands.Bot(command_prefix=commandPrefix)
#bot = commands.Bot(command_prefix="!")
global ae1
global ae2
ae1 = 0
ae2 = 0
TOKEN = input("Token : ")

@bot.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send("Tu n'est pas de la bonne équipe")

@bot.command(name='dit', help="Dit ce qut tu veut", category="Autre")
async def dit(ctx, arg):
    await ctx.send(arg)

@bot.command(name="setAe1", help="Permet de regler l'argent de l' équipe 1")
@commands.has_role("Admin")
async def dit(ctx, argent:int):
    global ae1
    argent = int(argent)
    ae1 = argent
    reponse = "l'argent est bien mi"
    await ctx.send(reponse)
    reponse = ae1
    await ctx.send(reponse)

@bot.command(name="setAe2", help="Permet de regler l'argent de l' équipe 2")
@commands.has_role("Admin")
async def dit(ctx, argent):
    global ae2
    argent = int(argent)
    ae2 = argent
    reponse = "l'argent est bien mi"
    await ctx.send(reponse)
    reponse = ae2
    await ctx.send(reponse)

@bot.command(name="money", help="Monter combien d'argent tu à")
async def dit(ctx):
    global ae1
    global ae2
    reponse = "L'équipe 2 à : "
    await ctx.send(reponse)
    reponse = ae2
    await ctx.send(reponse)
    reponse = "L'équipe 1 à : "
    await ctx.send(reponse)
    reponse = ae1
    await ctx.send(reponse)

@bot.command(name='workE1', help="Permet de gagner de l'argent fictive pour l'équipe 1")
@commands.has_role("E1")
async def workE1(ctx):
    global ae1
    r = random.randint(50,500)
    ae1 += r
    reponse = "Tu a gagner : "
    await ctx.send(reponse)
    await ctx.send(r)
    reponse = "Tu a maintenant : "
    await ctx.send(reponse)
    await ctx.send(ae1)

@bot.command(name='workE2', help="Permet de gagner de l'argent fictive pour l'équipe 2")
@commands.has_role("E2")
async def workE1(ctx):
    global ae2
    r = random.randint(50,500)
    reponse = "Tu a gagner : "
    await ctx.send(reponse)
    await ctx.send(r)
    reponse = "Tu a maintenant : "
    await ctx.send(reponse)
    ae2 = r +ae2
    await ctx.send(ae2)

@bot.command(name="save", help="permet de sovegarder les donées")
async def save(ctx):
    global ae1
    global ae2
    fichier = open("saveE1.txt", "w")
    ae1str = str(ae1)
    print(ae1str)
    #fichier.write(ae1str)
    fichier.write(ae1str)
    fichier.close()
    fichier = open("saveE2.txt", "w")
    ae2str = str(ae2)
    fichier.write(ae2str)
    fichier.close()

bot.run(TOKEN)
