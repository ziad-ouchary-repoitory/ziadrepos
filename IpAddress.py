import socket

hostName = input("Inserisci l'host per scoprire l'indirizzo IP: ")

print(f"L'indirizzo IP di {hostName} è: {socket.gethostbyname(hostName)}")