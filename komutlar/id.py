import hikari
import lightbulb


plugin = lightbulb.Plugin("zarlar")


@plugin.command
@lightbulb.command("id", "Kullanıcı ID'nizi öğrenin.")
@lightbulb.implements(lightbulb.SlashCommand)
async def id(ctx):
    await ctx.respond(hikari.Embed(title=f"Kullanıcı ID'niz:", description=ctx.author.id, colour="#FFA500",))


def load(bot):
    bot.add_plugin(plugin)
