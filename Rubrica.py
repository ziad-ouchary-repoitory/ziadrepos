from Contatto import Contatto

contatti = [Contatto]

class Rubrica:
    def AggiungiNuovoContatto():
        c = Contatto()

        c.set_nome = input("Inserisci il nome del nuovo contatto: ")
        c.set_cognome = input("Inserisci il cognome del nuovo contatto: ")
        c.set_telefono = input("Inserisci il telefono del nuovo contatto: ")
        c.set_email = input("Inserisci l'email del nuovo contatto: ")

        return c

    def Aggiungi():
        contatti.append(Rubrica.AggiungiNuovoContatto())

    def Elimina():
        indice = -1

        nome = input("Inserisci il nome del contatto da eliminare: ")
        cognome = input("Inserisci il cognome del contatto da eliminare: ")

        for i in contatti.count:
            if nome == contatti[i].get_nome() and cognome == contatti[i].get_cognome():

                indice = i

        return indice

    def EliminaContatto():
        contatti.remove(Rubrica.Elimina())

    def VisualizzaContatti():
        elenco = ""

        for i in contatti.count:
            elenco += contatti[i].ToString()+"\n\n"
        return elenco