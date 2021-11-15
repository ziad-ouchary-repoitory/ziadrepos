class Menu:

    def ___init__(self):
        pass

    def MostraMenu():
        print("1 per aggiungere un Contatto.")
        print("2 per rimuovere un Contatto.")
        print("3 per visualizzare tutta la Rubrica.")
        print("4 per uscire dal programma.")
        print("-->", end="")

    def Scelta():
        scelta = ''

        Menu.MostraMenu()
        scelta = input()

        return scelta