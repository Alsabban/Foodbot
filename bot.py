from rivescript import RiveScript

bot = RiveScript(utf8=True)
bot.load_directory('Brain')
bot.sort_replies()


def chat(message):
    if message == "":
        return -1, "No message was sent"
    else:
        response = bot.reply("user", message)
    if response:
        return 0, response
    else:
        return -1, "No reply found"



