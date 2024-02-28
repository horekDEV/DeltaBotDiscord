import disnake
from disnake.ext import commands

import StartBot

bot = commands.Bot(command_prefix="?",
                   help_command=None, intents=disnake.Intents.all(),
                   test_guilds=[1152846833341710368])

censored_words = [
    "даун", "блядь", "блять", "ебал", "fuck", "уебок",
    "ублюдок", "далбаеб", "шлюха", "хуй", "пизда", "pizda",
    "аутист", "пиздаболл", "пиздабол", "ебанный", "пидр", "пидарас",
    "пидорок", "еблан", "ебло", "конч", "конченный", "конча",
    "блудилище", "гондон", "гондурас", "дрочить", "елдище", "залупа",
    "кретин", "мудак", "кретин", "мудазвон", "спид", "спидос",
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
    await bot.process_commands(message)

    for word in censored_words:
        for cont in message.content.split():
            if cont.lower() == word:
                await message.delete()
                await message.channel.send(f"{message.author.mention} Воу Воу, давай-ка обойдемся без матов :)",
                                           delete_after=3)


# moderation commands?
@bot.slash_command()
@commands.has_permissions(administrator=True)
async def kick(inter, member: disnake.Member, *, reason=None):
    await member.kick(reason=reason)
    await member.send(f"вас кикнули с сервера DeltaShop по причине: {reason}", delete_after=5)


@bot.slash_command()
@commands.has_permissions(administrator=True)
async def ban(inter, member: disnake.Member, *, reason=None):
    await member.ban(reason=reason)
    await member.send(f"вас забанили на сервере DeltaShop по причине: {reason}", delete_after=5)


@bot.slash_command()
@commands.has_permissions(administrator=True)
async def unban(inter, member: disnake.Member):
    await member.unban(reason=None)


@bot.slash_command()
@commands.has_permissions(administrator=True)
async def mute(inter, member: disnake.Member, time: int, *, reason=None):
    await member.timeout(duration=time, reason=reason)

    await inter.response.send_message(f"пользователь {member.mention} был замучен на {time} минут", delete_after=5)
    await member.send(f"Вам был выдан timeout на сервере DeltaShop по причине: {reason}")
    await member.send("Если наказание было выданно по ошибке, обращайтесь к модератору DeltaShop или администратору в "
                      "личные сообщения")


@bot.slash_command()
@commands.has_permissions(administrator=True)
async def clear(ctx, inter, amount: int):
    await ctx.channel.purge(amount=amount)

    await inter.response.send_message(f"Администратор {ctx.author.mention} удалил сообщения из чата DeltaShop",
                                      delete_after=10)


@bot.slash_command()
@commands.has_permissions(administrator=True)
async def give_oral_warn(inter, member: disnake.Member):
    role = disnake.utils.get(member.guild.roles, id=1190667354791759934)

    await member.add_roles(role)
    await member.send(f"Вам было выданно устное предупреждение!", delete_after=5)
    await inter.response.send_message(f"игроку {member.mention} было выданно устное предупреждение")


@bot.slash_command()
@commands.has_permissions(administrator=True)
async def give_warn(inter, member: disnake.Member):
    role = disnake.utils.get(member.guild.roles, id=1190667593741246594)
    await member.add_roles(role)
    await member.send(f"Вам было выданно предупреждение!")
    await inter.response.send_message(f"игроку было выданно предупреждение", delete_after=5)


@bot.slash_command()
@commands.has_permissions(administrator=True)
async def voting(inter, text=" "):
    message = f"@everyone \n {text}"
    await inter.send(message)
    await message.add_reaction("✅")
    await message.add_reaction("⛔️")


# user commands?
@bot.slash_command()
async def navigate(inter):
    await inter.response.send_message(f"\n все расценки на товары вы можете найти в: price_list💰"
                                      f"\n все важные новости по нашему проекту в: announcements📣"
                                      f"\n все правила нашего дискорд сервера находятся в: rules📖"
                                      f"\n здесь вы можете создать жалобу на игрока или сделать заказ: create_ticket📓"
                                      f"\n в этом канале вы можете общаться с другими участниками сервера: main_chat💌",
                                      delete_after=50)


@bot.slash_command()
async def social_media(inter):
    await inter.response.send_message(f"🖥️ наш телеграмм канал: https://t.me/deltashoptg \n"
                                      f"🎥 наш ютуб канал: https://www.youtube.com/channel/UCcN5QBp5OA3A6M8Ave-kS0A \n"
                                      f"🗃️ наш дискорд сервер(на котором вы находитесь🥹): "
                                      f"https://discord.gg/aZsFWpBvJq \n", delete_after=50)


@bot.slash_command()
async def invite(inter):
    await inter.response.send_message(f"https://discord.gg/aZsFWpBvJq - ссылка для приглашения на сервер", delete_after=50)


@bot.slash_command()
async def bot_info(inter):
    await inter.response.send_message(f"bot id/name: {bot} \n"
                                      f"bot version: 1.0.0 \n"
                                      f"bot author: horekdev \n", delete_after=50)


StartBot.start(bot_for_start=bot)
