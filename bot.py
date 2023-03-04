import asyncio
import hikari
import lightbulb
import random
import config


bot = lightbulb.BotApp(
    config.token,
    default_enabled_guilds=(config.enabled_guilds), intents=hikari.Intents.ALL_UNPRIVILEGED
)

bot.load_extensions_from("./komutlar")

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print("Ördek BOT by Naransula#0001")

@lightbulb.Check
def rp_mod(context: lightbulb.Context) -> bool:
    return context.author.id == config.rp_mods

@lightbulb.Check
def owner(context: lightbulb.Context) -> bool:
    return context.author.id == config.owner_id

@bot.command
@lightbulb.option("cümle", "Söylenecek cümle.")
@lightbulb.command("ooc", "OOC Konuşmanızı sağlar!")
@lightbulb.implements(lightbulb.SlashCommand)
async def yaz(ctx):
    proxy = await ctx.respond(f"// {ctx.author.mention}: {ctx.options.cümle}")
    message = await proxy.message()     
    await asyncio.sleep(10)
    await message.delete()

@bot.command
@lightbulb.add_checks(owner)
@lightbulb.option("cümle", "Söylenecek cümle.")
@lightbulb.command("söyle", "Botu konuşturur!")
@lightbulb.implements(lightbulb.SlashCommand)
async def yaz(ctx):
    await ctx.respond(hikari.Embed(title="Naransula diyor ki:", description=ctx.options.cümle, colour="#FFA500"))

@bot.command
@lightbulb.command("id", "Kullanıcı ID'nizi öğrenin.")
@lightbulb.implements(lightbulb.SlashCommand)
async def id(ctx):
    await ctx.respond(hikari.Embed(title=f"Kullanıcı ID'niz...", description=ctx.author.id, colour="#FFA500",))

bot.run()
