import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-"

all = lower + upper + numbers + symbols
length = int(input("Inserisci la lunghezza della password: "))
password = "".join(random.sample(all, length))
print("Password Generata: ", password)