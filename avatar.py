import discord
from discord.ext import commands
from datetime import datetime
import time
class avatar(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.command()
    async def avatar(self,ctx,member:discord.Member):
        embed = discord.Embed(title="Kullanıcı Avatar",color=discord.Color.red(),description=member.mention)
        embed.set_footer(text=member.display_name,icon_url=member.avatar_url)
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)
        await ctx.message.delete()



def setup(client):
    client.add_cog(avatar(client))