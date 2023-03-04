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

@bot.command
@lightbulb.command("id", "Kullanıcı ID'nizi öğrenin.")
@lightbulb.implements(lightbulb.SlashCommand)
async def id(ctx):
    await ctx.respond(hikari.Embed(title=f"Kullanıcı ID'niz...", description=ctx.author.id, colour="#FFA500",))

bot.run()
