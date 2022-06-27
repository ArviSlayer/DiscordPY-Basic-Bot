import discord
from discord.ext import commands
import sys
sys.path.insert(0, "C:\\Users\\ArviS\\Desktop\\DESKTOP\\DiscordPY-Basic-Bot\\admins")
import keys

class sustur(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.command()
    async def sustur(self,ctx,member:discord.Member,*,reason="yok"):
        

        
        guild = ctx.guild
        for rol in guild.roles:
            if rol.name=="Muted":
                if ctx.guild.id in keys.sahipler:
                    await member.add_roles(rol)
                    embed = discord.Embed(title="Susturuldu",description="{} tarafıdan".format(ctx.author.mention),color=discord.Color.red())
                    embed.set_footer(text="{} Susturuldu - Sebep: {}".format(member.display_name,reason),icon_url=member.avatar_url)
                    await ctx.send(embed=embed)
                    return
        

                overwrite = discord.PermissionOverwrite(send_messages=False)
                newRole = await guild.create_role(name="Muted")

                for channel in guild.text_channels:
                    await channel.set_permissions(newRole,overwrite=overwrite)

                    await member.add_roles(newRole)
                    embed = discord.Embed(title="Susturuldu",description="{} tarafından.".format(ctx.author.mention),color=discord.Color.red())
                    embed.set_footer(text="{} Susturuldu - Sebep: {}".format(member.display_name,reason),icon_url=member.avatar_url)
                    await ctx.send(embed=embed)
                else:
                    embed=discord.Embed(title="Upps",description="Bu Komutu Kullanabilecek Yetkin Bulunmuyor",color=discord.Color.red())
                    await ctx.send(embed=embed)
                    await ctx.message.delete()

    
    @commands.command()
    async def susturma(self,ctx,member:discord.Member):
        


        guild = ctx.guild
        for rol in guild.roles:
            if rol.name=="Muted":
                if ctx.guild.id in keys.sahipler:
                    await member.remove_roles(rol)
                    embed = discord.Embed(title="Susturma Açıldı {}, {} Tarafından.".format(member.display_name,ctx.author.mention),color=discord.Color.green())
                    embed.set_footer(text="{} Artık Konuşabilir".format(member.mention),icon_url=member.avatar_url)
                    await ctx.send(embed=embed)
                    return
            else:
                embed=discord.Embed(title="Başarısız",color=discord.Color.red())
                embed.set_footer(text="Bu Komutu Kullanabilecek Yetkin Bulunmuyor")
                await ctx.send(embed=embed)





def setup(client):
    client.add_cog(sustur(client))

