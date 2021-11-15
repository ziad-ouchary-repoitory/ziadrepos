import sys
import time
from threading import Thread

scelta = ""
conferma = ""
zucchero = 0
credito = 0
dovuto = 0
resto = 0

importoCaffe = 0.25
importoCaffeEspresso = 0.30
importoCaffeLungo = 0.30
importoCioccolata = 0.45
importoTheAlLimone = 0.30
importoCappuccino = 0.20
importoLatte = 0.20
importoGinseng = 0.70

print("\nBenvenuto Alla Macchinetta Del Caffè!")
print("\nPer uscire premi 9")

while True:
    print("\n01 - Caffè\t\t0.25 euro\n02 - Caffè Espresso\t0.30 euro\n03 - Caffè Lungo\t0.30 euro\n04 - Cioccolata\t\t0.45 euro\n05 - Thé al limone\t0.30 euro\n06 - Cappuccino\t\t0.20 euro\n07 - Latte\t\t0.20 euro\n08 - Ginseng\t\t0.70 euro\n09 - Esci")

    scelta = input("Scegli una bevanda o esci: ")

    if scelta == '1':
        print("\nHai selezionato Caffè")
        zucchero = int(input("\nScegli quanto zucchero max 5: "))
        while zucchero > 5:
            print("\nInserisci zucchero giusto!")
            zucchero = int(input("\nScegli quanto zucchero max 5: "))

        monete = float(input("\nInserisci i soldi: "))

        if (monete == 0.05 or monete == 0.10 or monete == 0.20 or monete == 0.50 or monete == 1.00 or monete == 2.00):
            if monete < importoCaffe:
                while (monete < importoCaffe):
                    dovuto = importoCaffe - monete
                    print("\nIl tuo credito è: ", "%.2f" % monete, "Dovuto: ", "%.2f" %dovuto)
                    credito = float(input("\nInserisci i soldi mancanti: "))
                    monete += credito
                    if monete >= importoCaffe:
                        resto = monete - importoCaffe
                        print("\nPreparazione in corso", end="")
                        for i in range(5):
                            print('.', end="")
                            time.sleep(1)

            elif monete >= importoCaffe:
                resto = monete - importoCaffe
                print("\nPreparazione in corso", end="")
                for i in range(5):
                    print('.', end="")
                    time.sleep(1)

            print("\n\nBevanda pronta prelevare!")
            print("\nResto: ", "%.2f" % resto)

        else:
            print("\nMoneta Inesistente!")
            break

    elif scelta == '2':
        print("\nHai selezionato Caffè Espresso")
        zucchero = int(input("\nScegli quanto zucchero max 5: "))
        while zucchero > 5:
            print("\nInserisci zucchero giusto!")
            zucchero = int(input("\nScegli quanto zucchero max 5: "))

        monete = float(input("\nInserisci i soldi: "))

        if (monete == 0.05 or monete == 0.10 or monete == 0.20 or monete == 0.50 or monete == 1.00 or monete == 2.00):
            if monete < importoCaffeEspresso:
                while (monete < importoCaffeEspresso):
                    dovuto = importoCaffeEspresso - monete
                    print("\nIl tuo credito è: ", "%.2f" % monete, "Dovuto: ", "%.2f" % dovuto)
                    credito = float(input("\nInserisci i soldi mancanti: "))
                    monete += credito
                    if monete >= importoCaffeEspresso:
                        resto = monete - importoCaffeEspresso
                        print("\nPreparazione in corso", end="")
                        for i in range(5):
                            print('.', end="")
                            time.sleep(1)

            elif monete >= importoCaffeEspresso:
                resto = monete - importoCaffeEspresso
                print("\nPreparazione in corso", end="")
                for i in range(5):
                    print('.', end="")
                    time.sleep(1)

            print("\n\nBevanda pronta prelevare!")
            print("\nResto: ", "%.2f" % resto)

        else:
            print("\nMoneta Inesistente!")
            break

    elif scelta == '3':
        print("\nHai selezionato Caffè Lungo")
        zucchero = int(input("\nScegli quanto zucchero max 5: "))
        while zucchero > 5:
            zucchero = int(input("\n\nInserisci zucchero giusto max 5: "))

        monete = float(input("\nInserisci i soldi: "))

        if (monete == 0.05 or monete == 0.10 or monete == 0.20 or monete == 0.50 or monete == 1.00 or monete == 2.00):
            if monete < importoCaffeLungo:
                while (monete < importoCaffeLungo):
                    dovuto = importoCaffeLungo - monete
                    print("\nIl tuo credito è: ", "%.2f" % monete, "Dovuto: " , "%.2f" % monete)
                    credito = float(input("\nInserisci i soldi mancanti: "))
                    monete += credito
                    if monete >= importoCaffeLungo:
                        resto = monete - importoCaffeLungo
                        print("\nPreparazione in corso", end="")
                        for i in range(5):
                            print('.', end="")
                            time.sleep(1)

            elif monete >= importoCaffeLungo:
                resto = monete - importoCaffeLungo
                print("\nPreparazione in corso", end="")
                for i in range(5):
                    print('.', end="")
                    time.sleep(1)

            print("\n\nBevanda pronta prelevare!")
            print("\nResto: ", "%.2f" % resto)

        else:
            print("\nMoneta Inesistente!")
            break

    elif scelta == '4':
        print("\nHai selezionato Cioccolata")
        zucchero = int(input("\nScegli quanto zucchero max 5: "))
        while zucchero > 5:
            zucchero = int(input("\n\nInserisci zucchero giusto max 5: "))

        monete = float(input("\nInserisci i soldi: "))

        if (monete == 0.05 or monete == 0.10 or monete == 0.20 or monete == 0.50 or monete == 1.00 or monete == 2.00):
            if monete < importoCioccolata:
                while (monete < importoCioccolata):
                    dovuto = importoCioccolata - monete
                    print("\nIl tuo credito è: ", "%.2f" % monete, "Dovuto: ", "%.2f" % dovuto)
                    credito = float(input("\nInserisci i soldi mancanti: "))
                    monete += credito
                    if monete >= importoCioccolata:
                        resto = monete - importoCioccolata
                        print("\nPreparazione in corso", end="")
                        for i in range(5):
                            print('.', end="")
                            time.sleep(1)

            elif monete >= importoCioccolata:
                resto = monete - importoCioccolata
                print("\nPreparazione in corso", end="")
                for i in range(5):
                    print('.', end="")
                    time.sleep(1)

            print("\n\nBevanda pronta prelevare!")
            print("\nResto: ", "%.2f" % resto)

        else:
            print("\nMoneta Inesistente!")
            break

    elif scelta == '5':
        print("\nHai selezionato Thè Al Limone")
        zucchero = int(input("\nScegli quanto zucchero max 5: "))
        while zucchero > 5:
            zucchero = int(input("\nInserisci zucchero giusto max 5: "))

        monete = float(input("\nInserisci i soldi: "))

        if (monete == 0.05 or monete == 0.10 or monete == 0.20 or monete == 0.50 or monete == 1.00 or monete == 2.00):
            if monete < importoTheAlLimone:
                while monete < importoTheAlLimone:
                    dovuto = importoTheAlLimone - monete
                    print("\nIl tuo credito è: ", "%.2f" % monete, "Dovuto: ", "%.2f" % dovuto)
                    credito = float(input("\nInserisci i soldi mancanti: "))
                    monete += credito
                    if monete >= importoTheAlLimone:
                        resto = monete - importoTheAlLimone
                        print("\nPreparazione in corso", end="")
                        for i in range(5):
                            print('.', end="")
                            time.sleep(1)

            elif monete >= importoTheAlLimone:
                resto = monete - importoTheAlLimone
                print("\nPreparione in corso", end="")
                for i in range(5):
                    print('.', end="")
                    time.sleep(1)

            print("\n\nBevanda pronta prelevare")
            print("\nResto: ", "%.2f" % resto)

        else:
            print("\nMoneta Insesistente")
            break

    elif scelta == '6':
        print("\nHai selezionato Cappuccino")
        zucchero = int(input("\nScegli quanto zucchero max 5: "))
        while zucchero > 5:
            zucchero = int(input("\nInserisci zucchero giusto max 5: "))

        monete = float(input("\nInserisci i soldi: "))

        if (monete == 0.05 or monete == 0.10 or monete == 0.20 or monete == 0.50 or monete == 1.00 or monete == 2.00):
            if monete < importoCappuccino:
                while monete < importoCappuccino:
                    dovuto = importoCappuccino - monete
                    print("\nIl tuo credito è: ", "%.2f" % monete, "Dovuto: ", "%.2f" % dovuto)
                    credito = float(input("\nInserisci i soldi mancanti: "))
                    monete += credito
                    if monete >= importoCappuccino:
                        resto = monete - importoCappuccino
                        print("\nPreparazione in corso", end="")
                        for i in range(5):
                            print('.', end="")
                            time.sleep(1)

            elif monete >= importoCappuccino:
                resto = monete - importoCappuccino
                print("\nPreparione in corso", end="")
                for i in range(5):
                    print('.', end="")
                    time.sleep(1)

            print("\n\nBevanda pronta prelevare")
            print("\nResto: ", "%.2f" % resto)

        else:
            print("\nMoneta Insesistente")
            break

    elif scelta == '7':
        print("\nHai selezionato Latte")
        zucchero = int(input("\nScegli quanto zucchero max 5: "))
        while zucchero > 5:
            zucchero = int(input("\nInserisci zucchero giusto max 5: "))

        monete = float(input("\nInserisci i soldi: "))

        if (monete == 0.05 or monete == 0.10 or monete == 0.20 or monete == 0.50 or monete == 1.00 or monete == 2.00):
            if monete < importoLatte:
                while monete < importoLatte:
                    dovuto = importoLatte - monete
                    print("\nIl tuo credito è: ", "%.2f" % monete, "Dovuto: ", "%.2f" % dovuto)
                    credito = float(input("\nInserisci i soldi mancanti: "))
                    monete += credito
                    if monete >= importoLatte:
                        resto = monete - importoLatte
                        print("\nPreparazione in corso", end="")
                        for i in range(5):
                            print('.', end="")
                            time.sleep(1)

            elif monete >= importoLatte:
                resto = monete - importoLatte
                print("\nPreparione in corso", end="")
                for i in range(5):
                    print('.', end="")
                    time.sleep(1)

            print("\n\nBevanda pronta prelevare")
            print("\nResto: ", "%.2f" % resto)

        else:
            print("\nMoneta Insesistente")
            break

    elif scelta == '8':
        print("\nHai selezionato Ginseng")
        zucchero = int(input("\nScegli quanto zucchero max 5: "))
        while zucchero > 5:
            zucchero = int(input("\nInserisci zucchero giusto max 5: "))

        monete = float(input("\nInserisci i soldi: "))

        if (monete == 0.05 or monete == 0.10 or monete == 0.20 or monete == 0.50 or monete == 1.00 or monete == 2.00):
            if monete < importoGinseng:
                while monete < importoGinseng:
                    dovuto = importoGinseng - monete
                    print("\nIl tuo credito è: ", "%.2f" % monete, "Dovuto: ", "%.2f" % dovuto)
                    credito = float(input("\nInserisci i soldi mancanti: "))
                    monete += credito
                    if monete >= importoGinseng:
                        resto = monete - importoGinseng
                        print("\nPreparazione in corso", end="")
                        for i in range(5):
                            print('.', end="")
                            time.sleep(1)

            elif monete >= importoGinseng:
                resto = monete - importoGinseng
                print("\nPreparione in corso", end="")
                for i in range(5):
                    print('.', end="")
                    time.sleep(1)

            print("\n\nBevanda pronta prelevare")
            print("\nResto: ", "%.2f" % resto)

        else:
            print("\nMoneta Insesistente")
            break

    elif scelta == '9':
        sys.exit()

    conferma = input("Vuoi dell'altro? ")

    if conferma == "no":
        sys.exit()
    elif conferma == "si":
        continue