from os import replace
import pyodbc
import pandas as pd
from datetime import datetime

server = 'LAPTOP-R2PR10CM\SQLEXPRESS'
db = 'Magazzino'

conn = pyodbc.connect(driver='{SQL Server Native Client 11.0}',
                      host=server, database=db, trusted_connection='yes')

cursor = conn.cursor()

##INSERT DENTRO PRODOTTI E SELECT DI ESSA
""" SqlCommand = "INSERT INTO Prodotti (Marca, Prezzo, Codice, IdReparto) VALUES(?, ?, ?, ?)"

marca = input("Marca: ")
prezzo = input("Prezzo: ")
codice = input("Codice: ")
IdReparto = input("IdReparto: ")

values = [marca, prezzo, codice, IdReparto]

cursor.execute(SqlCommand, values)
conn.commit()
cursor.execute("SELECT * FROM PRODOTTI")
print("INSERIMENTO COMPLETATO CON SUCCESSO!")
for row in cursor:
    print(row) """

## PROVA DEL PARSE DELLA DATA DA STRINGA A DATE PASSANDO PER DATETIME
""" Sqlcommand = "INSERT INTO Date (data) VALUES(?)"

datetime_str = "180701"

datetime_obj = datetime.strptime(datetime_str, "%d%m%y")

date = datetime_obj.date()

values = [date]

cursor.execute(Sqlcommand, values)
cursor.commit()
 """

## INSERIMENTO NUOVO DIPENDENTE CON LA DATA PARSERIZZATA
""" SqlCommand = "INSERT INTO Dipendenti (Nome, Cognome, CodiceFiscale, DataNascita, Ruolo, IdReparto) VALUES(?,?,?,?,?,?)" """

""" nome = input("Nome: ")
cognome = input("Cognome: ")
codiceFiscale = input("Codice Fiscale: ")

dataNascita_str = input("Data Di Nascita: ")
dataNascita_obj = datetime.strptime(dataNascita_str, "%d%m%y")
dataNascita = dataNascita_obj.date()

ruolo = input("Ruolo: ")
idReparto = input("ID Reparto: ")

values = [nome, cognome, codiceFiscale, dataNascita, ruolo, idReparto]

conn.execute(SqlCommand, values)
conn.commit()

print("INSERIMENTO EFFETTUATO CON SUCCESSO!")
print() 

cursor.execute("SELECT * FROM Dipendenti")

for row in cursor:
    print(row)"""


""" ## UPDATE DIPENDENTE
cursor.execute("SELECT * FROM Dipendenti")
for i in cursor:
    print(i)

SqlCommand = "UPDATE Dipendenti SET CodiceFiscale = ? WHERE IdDipendente = ?"

codiceFiscale = input("Nuovo Codice Fiscale: ")
Id = input("ID: ")

values = [codiceFiscale, Id]

cursor.execute(SqlCommand, values)
cursor.commit()

print("Codice Ficale Aggiornato Con Successo!")

cursor.execute("SELECT * FROM Dipendenti")
for i in cursor:
    print(i) """


## DELETE DIPENDENTE

""" cursor.execute("SELECT * FROM Dipendenti")
for i in cursor:
    print(i)


SqlCommand = "DELETE FROM Dipendenti WHERE IdDipendente = ?"
eliminato = input("ID Dipendente da eliminare: ")

cursor.execute(SqlCommand, eliminato)
cursor.commit()

print("DIPENDENTE ELIMINATO CON SUCCESSO!")
 """

## Retrive data from sql and manage it into arrays and more
cursor.execute("SELECT Nome, Cognome FROM Dipendenti")
result = cursor.fetchall()

n = []
c = []

for i in result:
    nomi = i[0]
    cognomi = i[1]
    n.append(nomi)
    c.append(cognomi)

    
print("Il primo nome e cognome è: ", n[0] , "",  c[0], "\nIl Secondo nome e cognome è: ", n[1], "", c[1])


conn.close()