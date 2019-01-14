import time
import discord #importer la librairie discord.py
from discord.ext import commands #importer des commandes spécifiques de la librairie
from discord.utils import find
import os
bot = commands.Bot(command_prefix = 'l!') #indiquez la description et le préfixe de votre bot (laissez les apostrophes)
bot.remove_command('help')
NerincetClientID = ('526175855609905162')

@bot.event
async def on_guild_join(guild, ctx):
    print("Un nouveau serveur nous a rejoint!")
    message = discord.Embed(description="Merci de m'avoir ajouté dans votre serveur!", title='Lanfangen Nelicet, prêt à vous servir!', color=0x640066) 
    message.set_thumbnail(url="http://image.noelshack.com/fichiers/2018/52/2/1545753334-soliman.jpg")
    message.add_field(name="Rejoins le serveur du bot!", value="lien", inline=False)
    message.set_footer(text="Introduit depuis la 1.0.0.0")
    await ctx.author.send(embed=message==guild)
@bot.command()
async def ping(ctx):
    pingj = bot.latency
    ping = round(pingj *1000)
    """Renvoie 'Pong !'""" #description de la commande (affichée dans le message d'aide)
    await ctx.send("Pong ! Ton ping est de " + str(ping) + " millisecondes, " + ctx.author.mention) #réponse du bot


@bot.command(pass_context=True)
async def parrot(ctx, *, text):
    if ctx.message.author.id == int("526175855609905162"):
        await ctx.send(text)       
    else:
        await ctx.send("Désolé, seulement mon maître peut utiliser cette commande.")


@bot.command(pass_context=True)
async def help(ctx):

    message = discord.Embed(description="Commandes d'aide: Général", title='*Aide pour le Profil*', color=0x640066) 
    
    """Affiche l'aide ici."""
    message.set_thumbnail(url="http://image.noelshack.com/fichiers/2018/52/2/1545753334-soliman.jpg")
    message.add_field(name="l!open", value="Vous ouvre un compte. 1 compte par personne max!.", inline=False)
    message.add_field(name="~~l!profile~~", value="Affiche votre profil dans le jeu.", inline=False)
    message.add_field(name="~~l!profile @mentionné~~", value="Affiche le profil du mentionné.", inline=False)
    message.add_field(name="=Alias:", value="~~l!p~~", inline=False)
    message.add_field(name="~~l!check~~", value="Permet de récupérer son argent.", inline=False)
    message.add_field(name="Alias:", value="Aucun", inline=False)  
    message.add_field(name="~~l!check~~ ~~>h<~~ ~~>d<~~ ~~>w<~~", value="Permet de récupérer son argent respectivement horaire, quotidien, ou hebdomadaire.", inline=False)
    message.add_field(name="Alias:", value="Aucun", inline=False)
    message.add_field(name="~~l!balance~~", value="Permet de voir la quantité de jetons lanfangistes que vous avez.", inline=False)
    message.add_field(name="Alias", value="~~l!bal~~", inline=False)
    message.add_field(name="~~l!parrot~~", value="Répète tout ce que vous dites!", inline=False)
    message.add_field(name="Alias", value="~~l!echo~~ ~~l!say~~", inline=False)
    message.set_footer(text="Créée depuis la 1.0.0.0 Alpha")
    message.set_author(name="Commandes d'aide", icon_url="http://image.noelshack.com/fichiers/2018/52/2/1545753334-soliman.jpg")
    await ctx.author.send(embed=message)
    

@bot.command()
async def open(ctx):
    """Ouvre votre compte de jeux."""
    await ctx.send("Votre compte à bien été configuré!")

@bot.event
async def on_ready():
    print("Prêt à vous servir, maître.")
    print("Je sers : " + str(len(bot.guilds)) + " serveurs actuellement, et je sers " + str(len(set(bot.get_all_members()))) + " personnes !")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="(l!help)Ya salam! Je suis dans " + str(len(bot.guilds)) + " serveurs!"))
bot.run(bot.run(os.environ[TOKEN])) #Lancer le bot. Remplacez token par votre token et laissez les apostrophes    



