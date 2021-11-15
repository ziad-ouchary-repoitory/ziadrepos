import Menu
import Rubrica
import sys

r = Rubrica()

scelta = ''

mioMenu = Menu()

while True:
    scelta = mioMenu.Scelta()

    if scelta == '1':
        r.Aggiungi()
        break
    elif scelta == '2':
        r.EliminaContatto()
        break
    elif scelta == '3':
        elenco = r.VisualizzaContatti()
        print(elenco)
        print("Premi invio per continuare")
        break
    elif scelta == '4':
        sys.exit()
    else:
        print("Attenzione valore inserito non valido")
        print("Premi invio per continuare")
        scelta = mioMenu.Scelta()