from discord.ext import commands
import discord
import requests
from bs4 import BeautifulSoup

class döviz(commands.Cog):
    def __init__(self,client):
        self.client=client

    
    @commands.command()
    async def döviz(self,ctx,int=1):
        r=requests.get("https://www.doviz.com")
        x=requests.get("https://www.doviz.com/kripto-paralar/ethereum")
        soup = BeautifulSoup(r.content,"html.parser")
        soup1 = BeautifulSoup(x.content,"html.parser")
        veri = soup.find_all('span',attrs={'class':'value'})
        veri2 = soup1.find_all('span',attrs={'class':'value'})
        altın = veri[0].text
        dolar = veri[1].text
        euro = veri[2].text 
        bitcoin = veri[5].text
        ethereum = veri2[19].text
        embed=discord.Embed(title="Güncel Döviz Kurları ve Borsaları",inline=False)
        embed.add_field(name="Gram Altın",value=":chart_with_downwards_trend: {} ₺".format(altın),inline=False)
        embed.add_field(name="Dolar",value=":chart_with_downwards_trend: {} ₺".format(dolar),inline=False)
        embed.add_field(name="Euro",value=":chart_with_downwards_trend: {} ₺".format(euro),inline=False)
        embed.add_field(name="Bitcoin",value=":chart_with_downwards_trend: {}".format(bitcoin),inline=False)
        embed.add_field(name="Ethereum",value=":chart_with_downwards_trend: {}".format(ethereum),inline=False)
        embed.set_thumbnail(url="https://i1.sndcdn.com/avatars-QaAQt9v7rY2Co145-bciOpg-t240x240.jpg")
        await ctx.send(embed=embed)
        await ctx.message.delete()


def setup(client):
    client.add_cog(döviz(client))