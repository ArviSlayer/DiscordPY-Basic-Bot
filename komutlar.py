import discord
from discord.ext import commands

class komutlar(commands.Cog):
    def __init__(self,client):
        self.client=client



    @commands.command()
    async def komutlar(self,ctx):
        embed = discord.Embed(title="Komut Listesi")
        
        embed.add_field(name="Avatar",value="!avatar <@Kullanıcı>")
        embed.add_field(name="Döviz",value="!döviz")
        embed.add_field(name="Kullanıcı Bilgi",value="!kullanıcı")
        embed.add_field(name="Sustur",value="!sustur")
        embed.add_field(name="Mesaj Silme",value="!sil <Mesaj Miktarı>")


        await ctx.send(embed=embed)
        await ctx.message.delete()



def setup(client):
    client.add_cog(komutlar(client))