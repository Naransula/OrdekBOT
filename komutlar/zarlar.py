import hikari
import lightbulb
import random

plugin = lightbulb.Plugin("zarlar")

@plugin.command
@lightbulb.command("zar", "Tüm zar komutları bir yerde!")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def zar_parent(ctx):
    pass

@zar_parent.child
@lightbulb.command("2", "2lik bir zar atar.")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def zar2(ctx):
    r2=(random.randint(1,2))
    await ctx.respond(hikari.Embed(title=f"Zar sonucu: {r2}", description="Buraya yazacak bişey bulamadım.",colour="#FFA500"))

@zar_parent.child
@lightbulb.command("15", "15lik bir zar atar.")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def zar15(ctx):
    r15=(random.randint(1,15))
    await ctx.respond(hikari.Embed(title=f"Zar sonucu: {r15}", description="Buraya yazacak bişey bulamadım.",colour="#FFA500"))

@zar_parent.child
@lightbulb.command("çatışma", "Çatışmalarda kullanılan 10luk bir zar atar.")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def zarcatisma(ctx):
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

def load(bot):
    bot.add_plugin(plugin)
