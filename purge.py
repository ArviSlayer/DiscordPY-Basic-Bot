import discord
from discord.ext import commands
import time

class purge(commands.Cog):
    def __init__(self,client):
        self.client=client
    
    @commands.command()
    async def sil(self,ctx,miktar=50):
        await ctx.channel.purge(limit=miktar)
        embed = discord.Embed(title="Mesaj Temizleme",color=discord.Color.green())
        embed.add_field(name="{} Adet Mesaj Başarıyla Temizlendi,".format(miktar),value=":white_check_mark:")
        
        await ctx.send(embed=embed,delete_after=5)
        
        

def setup(client):
    client.add_cog(purge(client))
    