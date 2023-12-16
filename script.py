import disnake
from disnake.ext import commands

import StartBot

bot = commands.Bot(command_prefix="?", help_command=None, intents=disnake.Intents.all())

censored_words = [
    "даун", "блядь", "блять", "ебал", "fuck", "уебок",
    "ублюдок", "далбаеб", "шлюха", "хуй", "пизда", "pizda",
    "аутист", "пиздаболл", "пиздабол", "ебанный", "пидр", "пидарас",
    "пидорок", "еблан", "ебло", "конч", "конченный", "конча",
    "блудилище", "гондон", "гондурас", "дрочить", "елдище", "залупа"
    "кретин", "мудак", "кретин", "мудазвон", "спид", "спидос"
    "хрен", "ахуеть", "ахуел", "сук", "бл", "нах",
    "ссанина", "очко", "блядина", "ебланище", "влагалище", "пшлнх"
]


# default events
@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    print("------")

    await bot.change_presence(status=disnake.Status.idle,
                              activity=disnake.Activity(type=disnake.ActivityType.watching))


@bot.event
async def on_message(message):
    for word in censored_words:
        for cont in message.content.split():
            if cont == word:
                await message.delete()
                await message.channel.send(f"{message.author.mention} Воу Воу, давай-ка обойдемся без матов :)",
                                           delete_after=3)


# moderation commands?
@bot.command()
@commands.has_permissions(administrator=True)
async def kick(member: disnake.Member, *, reason=None):
    await member.kick(reason=reason)
    await member.send(f"вас кикнули с сервера DeltaShop по причине: {reason}")


@bot.command()
@commands.has_permissions(administrator=True)
async def ban(member: disnake.Member, *, reason=None):
    await member.ban(reason=reason)
    await member.send(f"вас забанили на сервере DeltaShop по причине: {reason}")


@bot.command()
@commands.has_permissions(administrator=True)
async def unban(member: disnake.Member):
    await member.unban(reason=None)


@bot.command()
@commands.has_permissions(administrator=True)
async def mute(member: disnake.Member, time: float, *, reason=None):
    await member.timeout(duration=time, reason=reason)
    await member.send(f"Вам был выдан timeout на сервере DeltaShop по причине: {reason}")
    await member.send("Если наказание было выданно по ошибке, обращайтесь к модератору DeltaShop или администратору в "
                      "личные сообщения")


@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(amount=amount)
    await ctx.send(f"Администратор {ctx.author.mention} удалил сообщения из чата DeltaShop", delete_after=10)


@bot.command()
@commands.has_permissions(administrator=True)
async def give_oral_warn(member: disnake.Member, role: disnake.Role):
    await member.add_roles(role)
    await member.send(f"Вам было выданно устное предупреждение!")


@bot.command()
@commands.has_permissions(administrator=True)
async def give_warn(member: disnake.Member, role: disnake.Role):
    await member.add_roles(role)
    await member.send(f"Вам было выданно предупреждение!")

StartBot.start(bot_for_start=bot)
