from os import replace
import pyodbc
import pandas as pd
from datetime import datetime
from colorama import Fore, Style

from SQLclass import SQLConnection

server = 'LAPTOP-R2PR10CM\SQLEXPRESS'
db = 'Magazzino'

sql = SQLConnection(server, db)

##query = "UPDATE Dipendenti SET CodiceFiscale = ? WHERE IdDipendente = ?"
query = "INSERT INTO Dipendenti (Nome, Cognome, CodiceFiscale, DataNascita, Ruolo, IdReparto) VALUES(?,?,?,?,?,?)"

dataNascita_str = '140998'
dataNascita_obj = datetime.strptime(dataNascita_str, "%d%m%y")
dataNascita = dataNascita_obj.date()

values = ['Flavio', 'Rottigni', 'dsfjdsdlskfj', dataNascita, 'Stagista', 2]

##values = ["RSSMRA01A01F205G", 7]

sql.operation(query, values)

print(Fore.GREEN + 'AGGIORNATO CON SUCCESSO!')
print(Style.RESET_ALL)

sql.get_closeConn()

















""" conn = pyodbc.connect(driver='{SQL Server Native Client 11.0}',
                      host=server, database=db, trusted_connection='yes')

cursor = conn.cursor()

cursor.execute("UPDATE Dipendenti SET CodiceFiscale = ? WHERE IdDipendente = ?", 'RSSMRA01A01F205G', 3)
cursor.commit()

print("Codice Ficale Aggiornato Con Successo!")

cursor.execute("SELECT * FROM Dipendenti")
for i in cursor:
    print(i)


conn.close() """