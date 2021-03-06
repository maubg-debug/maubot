import random
import discord
import urllib
import secrets
import asyncio
import aiohttp
import re

from io import BytesIO
from discord.ext import commands 
from . import http

from os import environ as env

color =   int(env["COLOR"])
class Animales(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    async def randomimageapi(self, ctx, url, endpoint):
        try:
            r = await http.get(url, res_method="json", headers={"Authorization": env["API_FLEX"]})
        except aiohttp.ClientConnectorError:
            return await ctx.send("La api esta abajo...")
        except aiohttp.ContentTypeError:
            return await ctx.send("La Api no devolvio un JSON...")
            
        embed = discord.Embed(colour=color)
        embed.set_image(url=r[endpoint])
        await ctx.send(embed=embed)

    @commands.command(description="Imagenes de gatos")
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def cat(self, ctx):
        await self.randomimageapi(ctx, 'https://api.alexflipnote.dev/cats', 'file')

    @commands.command(description="Imagenes de perros")
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def dog(self, ctx):
        await self.randomimageapi(ctx, 'https://api.alexflipnote.dev/dogs', 'file')

    @commands.command(aliases=["bird"], description="Imagenes de pajaros")
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def birb(self, ctx):
        await self.randomimageapi(ctx, 'https://api.alexflipnote.dev/birb', 'file')

    @commands.command(description="Imagenes random de patitos")
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def duck(self, ctx):
        await self.randomimageapi(ctx, 'https://random-d.uk/api/v1/random', 'url')

    @commands.command(description="¿Cafes?")
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def coffee(self, ctx):
        await self.randomimageapi(ctx, 'https://coffee.alexflipnote.dev/random.json', 'file')


    @commands.command(description="Imagenes random de zorros")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def fox(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://randomfox.ca/floof/") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Floof", colour=color)
                    embed.set_image(url=data['image'])
                    embed.set_footer(text="https://randomfox.ca/")

                    await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Animales(bot))
