from bot import *

@bot.message_handler(commands=["start"])
def who_developer(message):
    bot.send_message(message.chat.id, """Привет. Мои боты:
@Willy_horoskope_bot
@KaliLinuxHelpBot

@ChaplinBurger_bot (не доконченный с багом. +опыт)""")

@bot.message_handler(content_types=['text'])
def spam(message):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id,  "/start")

def main():
    bot.polling(none_stop=True)

if __name__ == '__main__':
    main()
