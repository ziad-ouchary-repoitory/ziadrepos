from pyodbc import Cursor
from SQLclass import SQLConnection
from datetime import datetime
server = 'LAPTOP-R2PR10CM\SQLEXPRESS'
db = 'Magazzino'


sqlConn = SQLConnection(server, db)


""" query = "INSERT INTO Dipendenti (Nome, Cognome, CodiceFiscale, DataNascita, Ruolo, IdReparto) VALUES(?,?,?,?,?,?)"

nome = input("Nome: ")
cognome = input("Cognome: ")
codiceFicale = input("CodiceFiscale: ")
dataNascita_str = input("Data Di Nascita: ")
dataNascita_obj = datetime.strptime(dataNascita_str, "%d%m%y")
dataNascita = dataNascita_obj.date()
ruolo = input("Ruolo: ")
idReparto = input("Id Reparto: ")

values = [nome, cognome, codiceFicale, dataNascita, ruolo, idReparto]

sqlConn.operation(query, values)
 """

selectQRY = "SELECT Nome, Cognome FROM Dipendenti"

sqlConn.query(selectQRY)

result = sqlConn.fetchall()

n = []
c = []

for i in result:
    nomi = i[0]
    cognomi = i[1]
    n.append(nomi)
    c.append(cognomi)

sqlConn.close()
    
