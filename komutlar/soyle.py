import hikari
import lightbulb
import config

plugin = lightbulb.Plugin("zarlar")


@lightbulb.Check
def owner(context: lightbulb.Context) -> bool:
    return context.author.id == config.owner_id

@plugin.command
@lightbulb.add_checks(owner)
@lightbulb.option("cümle", "Söylenecek cümle.")
@lightbulb.command("söyle", "Botu konuşturur!")
@lightbulb.implements(lightbulb.SlashCommand)
async def yaz(ctx):
    await ctx.respond(hikari.Embed(title="Bot sahibi diyor ki:", description=ctx.options.cümle, colour="#FFA500"))

    
def load(bot):
    bot.add_plugin(plugin)
