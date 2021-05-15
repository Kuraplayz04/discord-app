# Discord.pyの読み込み
import discord

# Discordへ接続するのに必要
client = discord.Client(activity=discord.Game(name='青鬼管理システム'))

# 自分のBotのアクセストークンを記入
TOKEN = "ODQyNzM1NDQxOTQxMTAyNjAy.YJ5oig.gi02R4PhTKuAtGecGecUt_QNgfE"

@client.event
async def joined(ctx, *, member: discord.Member):
    await ctx.send(f'{member} joined on {member.joined_at}')

# Bot起動時に実行される
@client.event
async def on_ready():
    print('ログインしました')


# メッセージを取得した時に実行される
@client.event
async def on_message(message):
    # Botのメッセージは除外
    if message.author.bot:
        return

    # 条件に当てはまるメッセージかチェックし正しい場合は返す
    def check(msg):
        return msg.author == message.author

    # /getとチャンネル上に打ち込むとBotが反応を示す
    if message.content.startswith("/f3"):
        # /getと打ち込まれたチャンネル上に下記の文章を出力
        await message.channel.send("Level:3")

        # ユーザーからのメッセージを待つ
        wait_message = await client.wait_for("message", check=check)
        an0 = '<@&825992683465080845>'
        an1 = '\n青鬼ごっこやります。（'
        an2 = '）\nKuraPlayz04\n\nver1.16.2'

        # メッセージを打ち込まれたのを確認すると下記の文章を出力
        channel = client.get_channel(825992683701010449)
        await channel.send(an0 + an1 + wait_message.content + an2)

    if message.content.startswith("/f2"):
            # /getと打ち込まれたチャンネル上に下記の文章を出力
        await message.channel.send("Level:2")

            # ユーザーからのメッセージを待つ
        wait_message = await client.wait_for("message", check=check)
        an0 = '<@&825992683465080845>'
        an1 = '\n青鬼ごっこやります。（'
        an2 = '）\nKuraPlayz04\n\nver1.16.2'

            # メッセージを打ち込まれたのを確認すると下記の文章を出力
        channel = client.get_channel(825992683701010450)
        await channel.send(an0 + an1 + wait_message.content + an2)


    if message.content.startswith("/f1"):
                # /getと打ち込まれたチャンネル上に下記の文章を出力
        await message.channel.send("Level:1")

                # ユーザーからのメッセージを待つ
        wait_message = await client.wait_for("message", check=check)
        an0 = '<@&825992683465080845>'
        an1 = '\n青鬼ごっこやります。（'
        an2 = '）\nKuraPlayz04\n\nver1.16.2'

                # メッセージを打ち込まれたのを確認すると下記の文章を出力
        channel = client.get_channel(825992683701010451)
        await channel.send(an0 + an1 + wait_message.content + an2)

    if message.content.startswith("/n3"):
        # /getと打ち込まれたチャンネル上に下記の文章を出力
        await message.channel.send("次 [lv3]")

        # ユーザーからのメッセージを待つ
        wait_message = await client.wait_for("message", check=check)
        ans1 = '\n次どぞ（'
        ans2 = '）'

        # メッセージを打ち込まれたのを確認すると下記の文章を出力
        channel = client.get_channel(825992683701010449)
        await channel.send(ans1 + wait_message.content + ans2)

    if message.content.startswith("/n2"):
            # /getと打ち込まれたチャンネル上に下記の文章を出力
        await message.channel.send("次 [lv2]")

            # ユーザーからのメッセージを待つ
        wait_message = await client.wait_for("message", check=check)
        ans1 = '\n次どぞ（'
        ans2 = '）'

            # メッセージを打ち込まれたのを確認すると下記の文章を出力
        channel = client.get_channel(825992683701010450)
        await channel.send(ans1 + wait_message.content + ans2)

    if message.content.startswith("/n1"):
                # /getと打ち込まれたチャンネル上に下記の文章を出力
        await message.channel.send("次 [lv1]")

                # ユーザーからのメッセージを待つ
        wait_message = await client.wait_for("message", check=check)
        ans1 = '\n次どぞ（'
        ans2 = '）'

                # メッセージを打ち込まれたのを確認すると下記の文章を出力
        channel = client.get_channel(825992683701010451)
        await channel.send(ans1 + wait_message.content + ans2)








    if message.content.startswith("/l3"):
        # /getと打ち込まれたチャンネル上に下記の文章を出力
        await message.channel.send("ラスト [lv3]")

        # ユーザーからのメッセージを待つ
        wait_message = await client.wait_for("message", check=check)
        ansl1 = '\nラストどうぞ（'
        ansl2 = '）'

        # メッセージを打ち込まれたのを確認すると下記の文章を出力
        channel = client.get_channel(825992683701010449)
        await channel.send(ansl1 + wait_message.content + ansl2)

    if message.content.startswith("/l2"):
            # /getと打ち込まれたチャンネル上に下記の文章を出力
        await message.channel.send("ラスト [lv2]")

            # ユーザーからのメッセージを待つ
        wait_message = await client.wait_for("message", check=check)
        ansl1 = '\nラストどうぞ（'
        ansl2 = '）'

            # メッセージを打ち込まれたのを確認すると下記の文章を出力
        channel = client.get_channel(825992683701010450)
        await channel.send(ansl1 + wait_message.content + ansl2)

    if message.content.startswith("/l1"):
                # /getと打ち込まれたチャンネル上に下記の文章を出力
        await message.channel.send("ラスト [lv1]")

                # ユーザーからのメッセージを待つ
        wait_message = await client.wait_for("message", check=check)
        ansl1 = '\nラストどうぞ（'
        ansl2 = '）'

                # メッセージを打ち込まれたのを確認すると下記の文章を出力
        channel = client.get_channel(825992683701010451)
        await channel.send(ansl1 + wait_message.content + ansl2)
# Botの実行
client.run(TOKEN)

