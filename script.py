import disnake
from disnake.ext import commands

import StartBot

command_sync_flags = commands.CommandSyncFlags.none()
command_sync_flags.sync_commands = False

bot = commands.Bot(command_prefix=".", command_sync_flags=command_sync_flags, help_command=None, intents=disnake.Intents.all())

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
                              activity=disnake.Game('наблюдать за сервером DeltaShop'))


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


@bot.command()
@commands.has_permissions(administrator=True)
async def voting(ctx, text):
    message = await ctx.send(f"@everyone \n {text}")
    await message.add_reaction("👍")
    await message.add_reaction("❌")


# user commands?
@bot.command()
async def navigate(ctx):
    await ctx.send(f"{ctx.author.mention} "
                   f"\n все расценки на товары вы можете найти в: price_list💰"
                   f"\n все важные новости по нашему проекту в: announcements📣"
                   f"\n все правила нашего дискорд сервера находятся в: rules📖"
                   f"\n здесь вы можете создать жалобу на игрока или сделать заказ: create_ticket📓"
                   f"\n в этом канале вы можете общаться с другими участниками сервера: main_chat💌")


@bot.command()
async def social_media(ctx):
    await ctx.send(f"{ctx.author.mention} "
                   f"🖥️ наш телеграмм канал: https://t.me/deltashoptg \n"
                   f"🎥 наш ютуб канал: https://www.youtube.com/channel/UCcN5QBp5OA3A6M8Ave-kS0A \n"
                   f"🗃️ наш дискорд сервер(на котором вы находитесь🥹): https://discord.gg/aZsFWpBvJq \n")


@bot.command()
async def invite(ctx):
    await ctx.author.send(f"https://discord.gg/aZsFWpBvJq - {ctx.author.mention} ссылка для приглашения на сервер")


@bot.command()
async def bot_info(ctx):
    await ctx.send(f"bot id/name: {bot} \n"
                   f"bot version: 1.0.0 \n"
                   f"bot author: horekdev \n")

StartBot.start(bot_for_start=bot)
