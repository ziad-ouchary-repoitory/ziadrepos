importo = 0.25
moneta = float(input("Inserisci i soldi: "))
resto = 0
credito = 0

if moneta == 0.05 or moneta == 0.10 or moneta == 0.20 or moneta == 0.50 or moneta == 1.00 or moneta == 2.00:

    while moneta < importo:
        print("Il tuo credito è: ", "%.2f" %moneta)
        credito = float(input("Inserisci i soldi mancanti alla cifra: "))
        moneta += credito
        if moneta >= importo:
            resto = moneta - importo
            print("Apposto Grazie ", "%.2f" %resto)
            break
else:
    print("Moneta Inesistente!")