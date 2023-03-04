import hikari
import lightbulb
import config

bot = lightbulb.BotApp(
    config.token,
    default_enabled_guilds=(config.enabled_guilds), 
	intents=hikari.Intents.ALL_UNPRIVILEGED
)

bot.load_extensions_from("./komutlar")

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print("Ördek BOT by Naransula#0001")

bot.run()
