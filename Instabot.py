from instabot import Bot
import os

userLogged = ""
passwordUser = ""
message = ""
userReceiver = ""
path = "config/hoxore6311_uuid_and_cookie.json"
path2 = "config/hoxore6311.checkpoint"
vett = [path, path2]

if os.path.isfile(path and path2):
    for i in range (2):
        os.remove(vett[i])
    print("Eliminati")

bot = Bot()
userLogged = input("Inserisci il nickname del profilo per accedere: ")
passwordUser = input("Inserisci la password del profilo: ")
message = input("Inserisci il messaggio da inviare: ")
userReceiver = input("Inserisci il nickname dell'utente ricevente: ")
bot.login(username=userLogged, password=passwordUser)
bot.send_message(message , userReceiver)
print("MESSAGGIO INVIATO CON SUCCESSO!")
bot.logout(username=userLogged)
