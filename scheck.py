import requests
import random
import time
import telethon.client
import threading
import os
import telebot

BOT_TOKEN="xxxxxxxxxx"  #token do seu bot no telegram

bot = telebot.TeleBot(BOT_TOKEN)
#espera mensagem /lista
@bot.message_handler(commands=['lista'])
def on_message(message):
    bot.reply_to(message, "Aqui está a lista de usuários disponíveis:")
    with open("new_users.txt", "r") as f:
        users = f.read().splitlines()
        string_with_all_users = "\n".join(users)
        bot.reply_to(message, string_with_all_users)

def check_user_exists(word):
    response = requests.get("https://www.steamcommunity.com/id/" + word)

    if "The specified profile could not be found." in response.text:
        print("Novo usuário encontrado: " + word)
        with open("new_users.txt", "a") as f:
            f.write(word + "\n")
    else:
        print("O usuário '" + word + "' já existe")
        time.sleep(random.randint(10, 25))

thread = threading.Thread(target=bot.polling)
thread.start()

with open("wordlist.txt", "r") as f:
    words = f.read().splitlines()
for word in words:
    check_user_exists(word)
