import discord
from discord.ext import commands
import json

color = 0x75aef5 

class AfkCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['AFK', 'away'])
    async def afk(self, ctx: commands.Context, *, razon: str = "AFK"):

        user = ctx.author

        with open("./json/afk.json", "r") as f:
            users = json.load(f)
        
        if str(user.id) in users:
            users[str(user.id)]["afk"] = "1"
        else:
            users[str(user.id)] = {}
            users[str(user.id)]["afk"] = "1"
            users[str(user.id)]["status"] = "False"

        with open("./json/afk.json", "w") as f:
            json.dump(users,f)        
        
        await ctx.send(embed=discord.Embed(title="Usuario AFK", description=f"{user.mention} Ha sido puesto en **AFK** por favor no lo molesteis", colour=color).add_field(name="Razon", value=razon))


    @commands.Cog.listener()
    async def on_message(self, message):
        user = message.author

        with open("./json/afk.json", "r") as f:
            users = json.load(f)

        if str(user.id) in users:   
    
            if users[str(user.id)]["status"] == "True":
                users[str(user.id)]["afk"] = "0"
                users[str(user.id)]["status"] = "False"

                await message.channel.send(embed=discord.Embed(title="Mira quien ha vuelto", description=f"{user.mention} ha vuelto de su descanso. **bienvenido**",colour=color))


            if users[str(user.id)]["afk"] == "1":
                users[str(user.id)]["status"] = "True"

            with open("./json/afk.json", "w") as f:
                json.dump(users,f)    

def setup(bot):
    bot.add_cog(AfkCmd(bot))