
import json

from os import environ as env

"""
Un Cog de anti espam
:Localizacion: ./src/madoreacion-cog/antiespam

    Retorna True si el id del servidor esta en la lista
    Al utilizar el comando se reversera el valor booleano -
    dado desde el principio, Como si fuera un not gate

Solo dara Falso si el servidor no esta en la lista ho si llega ha haver un error

    :params: Se necesita pasar el contexto, por eso en la llamada se utiliza un
    pass_context=True para pasar el contexto de discord

Tambien hay una clase de Json para no tener que repetir el mismo codigo todo 
el tiempo

Tambien se utilizara para futuras ideas
"""

class Json():
    def __init__(self, dir, modo, val):
        self.modo = modo
        self.dir = dir
        self.val = val

    def JsonM(self):
        if self.modo == "r":
            with open(self.dir, self.modo) as f:
                self.val = json.load(f)
            return self.val
        elif self.modo == "w":
            with open(self.dir, self.modo) as f:
                json.dump(self.val, f, indent=4)
        else:
            raise ValueError
            

class ayuda:
    def __init__(self):
        self.j = Json

class Decoradores(ayuda):

    async def EsEspam(self, ctx):
        seguridad = None
        seguridad = self.j(str(env["JSON_DIR"] + "ext/seguridad.json"), "r", seguridad).JsonM()
        
        async def decorador(ctx):
            if ctx.guild is None: return False
            if str(ctx.guild.id) in seguridad: 
                if seguridad[str(ctx.guild.id)] == True: 
                    return True
                else: return False
            else: return False
        
        return await decorador(ctx)
