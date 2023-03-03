import asyncio
import hikari
import lightbulb
import random
import config


bot = lightbulb.BotApp(
    config.token,
    default_enabled_guilds=(config.enabled_guild), intents=hikari.Intents.ALL_UNPRIVILEGED
)

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print("Ördek BOT by Naransula")

@lightbulb.Check
def rp_mod(context: lightbulb.Context) -> bool:
    return context.author.id == config.rp_mods

@lightbulb.Check
def owner(context: lightbulb.Context) -> bool:
    return context.author.id == config.owner_id


@bot.command
@lightbulb.command("çatışma_zarı", "Çatışmada kullanılan 10luk bir zar atar.")
@lightbulb.implements(lightbulb.SlashCommand)
async def zar10(ctx):
    r10=random.randint(1,10)
    miss="Mermi hedefi ıskaladı!"
    arm="Mermi hedefin koluna isabet etti!"
    leg="Mermi hedefin bacağına isabet etti!"
    body="Mermi hedefin vücuduna isabet etti! Hedef yanlızca 1 hamle daha yapabilecek!"
    head="Mermi hedefin kafasına isabet etti! Hedef öldü!"
    if r10==1:
        sonuc=miss
    elif r10==2:
        sonuc=miss
    elif r10==3:
        sonuc=miss
    elif r10==4:
        sonuc=miss
    elif r10==5:
        sonuc=arm
    elif r10==6:
        sonuc=arm
    elif r10==7:
        sonuc=leg
    elif r10==8:
        sonuc=body
    elif r10==9:
        sonuc=body
    elif r10==10:
        sonuc=head
    await ctx.respond(hikari.Embed(title=f"Zar sonucu: {r10}", description=sonuc,colour="#FFA500"))

@bot.command
@lightbulb.command("zar15", "15lik bir zar atar.")
@lightbulb.implements(lightbulb.SlashCommand)
async def zar15(ctx):
    r15=(random.randint(1,15))
    await ctx.respond(hikari.Embed(title=f"Zar sonucu: {r15}", description="Buraya yazacak bişey bulamadım.",colour="#FFA500"))

@bot.command
@lightbulb.command("zar2", "2lik bir zar atar.")
@lightbulb.implements(lightbulb.SlashCommand)
async def zar15(ctx):
    r2=(random.randint(1,2))
    await ctx.respond(hikari.Embed(title=f"Zar sonucu: {r2}", description="Buraya yazacak bişey bulamadım.",colour="#FFA500"))

#@bot.command
#@lightbulb.option("cümle", "Söylenecek cümle.")
#@lightbulb.command("ooc", "OOC Konuşmanızı sağlar!")
#@lightbulb.implements(lightbulb.SlashCommand)
#async def yaz(ctx):
    #proxy = await ctx.respond(f"// {ctx.author.mention}: {ctx.options.cümle}")
    #message = await proxy.message()     
    #await asyncio.sleep(10)
    #await message.delete()
# Bu komudu nasıl düzeltebileceğimi biliyorsanız, Discord Sunucumdan iletişime geçebilirsiniz!

@bot.command
@lightbulb.add_checks(owner)
@lightbulb.option("cümle", "Söylenecek cümle.")
@lightbulb.command("söyle", "Botu konuşturur!")
@lightbulb.implements(lightbulb.SlashCommand)
async def yaz(ctx):
    await ctx.respond(hikari.Embed(title="Bot sahibi diyor ki:", description=ctx.options.cümle, colour="#FFA500"))

@bot.command
@lightbulb.command("id", "Kullanıcı ID'nizi öğrenin.")
@lightbulb.implements(lightbulb.SlashCommand)
async def id(ctx):
    await ctx.respond(hikari.Embed(title=f"Kullanıcı ID'niz...", description=ctx.author.id, colour="#FFA500",))

bot.run()
