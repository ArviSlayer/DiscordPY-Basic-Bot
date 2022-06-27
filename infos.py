import  discord
from discord.ext import commands
from datetime import datetime
import sys
sys.path.insert(0, "C:\\Users\\ArviS\\Desktop\\DESKTOP\\DiscordPY-Basic-Bot\\admins")
import keys
class info(commands.Cog):
    def __init__(self,client):
        self.client=client

    
    @commands.command()
    async def stats(self,ctx):
        if ctx.author.id in keys.sahipler:

            embed=discord.Embed(title="Bilgi",color=discord.Color.green())
            embed.set_author(name="ArviS")
            embed.add_field(name="Ping",value=str(round(self.client.latency * 1000)) + ' ms')
            embed.timestamp=datetime.now()
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/990362728734556213/991099557083488306/unknown.png")
            await ctx.send(embed=embed)
            await ctx.message.delete()
        else:
            embed=discord.Embed(title="Upps",description="Bu Komutu Kullanabilecek Yetkin Bulunmuyor",color=discord.Color.red())
            await ctx.send(embed=embed)
            await ctx.message.delete()



def setup(client):
    client.add_cog(info(client))