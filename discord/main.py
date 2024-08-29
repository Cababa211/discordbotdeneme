import discord
from discord.ext import commands
import main2

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def sayi(ctx, s1, s2):
    await ctx.send(int(s1) + int(s2))

@bot.command()
async def img(ctx):
    if ctx.message.attachments:
        for i in ctx.message.attachments:
            await i.save(f"./images/{i.filename}")
            await ctx.send("Resminiz kaydedilmiştir.")
            sinif, skor = main2.bott(f"./images/{i.filename}")
            if sinif == 'Güvercinler\n':
                await ctx.send("Verdiğiniz resim güvercinler sınıfında")
            elif sinif[:-1] == 'Serçeler':
                await ctx.send("Verdiğiniz resim serçeler sınıfında")
            else:
                await ctx.send("Gönderdiğiniz resmi tanıyamadım")
    else:
        await ctx.send("Lütfen mesajınıza ek bir dosya ekleyiniz.")

bot.run("MTIwNTkxODc0MTc3OTQ0NzgzOQ.GvyToC.oK95c6Os2OcXMZhLsq8G3HaX32h9XHkrAkf3tM")