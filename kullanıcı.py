import discord
from discord.ext import commands


class kullanıcı(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.command()
    async def kullanıcı(self,ctx,member:discord.Member):
            myembed = discord.Embed(title=member.name,color=discord.Color.red())
            myembed.add_field(name="Durum",value=member.status,inline=False)
            myembed.add_field(name="Rol",value=member.top_role,inline=False)
            myembed.add_field(name="ID",value=member.id,inline=False)
            myembed.add_field(name="Hesap Oluşturulma Tarihi",value=member.created_at,inline=False)
            myembed.add_field(name="Sunucuya Katılma Tarihi",value=member.joined_at,inline=False)
            myembed.set_thumbnail(url=member.avatar_url)
            myembed.set_image(url="https://media.discordapp.net/attachments/990362728734556213/991099557083488306/unknown.png")
            await ctx.send(embed=myembed)
            await ctx.message.delete()


def setup(client):
    client.add_cog(kullanıcı(client))