import discord
from discord.ext import commands
import random
from roliador import Roliador
description = '''Soy RolBot9000, un ente interdimensional capaz de viajar entre los diferentes universos y mundos.

Tengo la capacidad analítica de predecir resultados heróicos y fatales si se me solicita. Bip...Bop...'''
bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    print('RolBot9000 iniciándose...')
    print(bot.user.name)
    print(bot.user.id)
    print('Sistemas 100%')
    print('------')


@bot.command(pass_context=True)
async  def roll(ctx, number: int, modo="Normal"):
    """Tira un número de D10"""
    roliador = Roliador()
    if modo == "cobarde":
        roliador.repeat = -1
    if(modo == "PROFETA"):
       respond = roliador.profeta(number)
    else:
        results = roliador.roll(number)
        respond = roliador.pretty_print_discord(ctx.message.author, results)

    await bot.say(respond)


@bot.command(pass_context=True)
async  def ndn(ctx, xdy: str):
    """Tira formato NdN"""
    number, faces = xdy.split('d', 1)
    roliador = Roliador(int(faces), -1)
    results = roliador.roll(int(number))
    respond = roliador.pretty_print_discord(ctx.message.author, results)

    await bot.say(respond)


@bot.command(pass_context=True)
async  def custom(ctx, *dices: int):
    """Tira lo que pongas"""
    roliador = Roliador(10, -1)
    results = roliador.custom_roll(dices)
    respond = roliador.custom_pretty_print_discord(ctx.message.author, results)

    await bot.say(respond)

bot.run('MzU2NzExNTA3NjYyNDcxMTY4.DJfVEA.uH_oYeDr96fSSI8fPoJ8x9RQ1vk')