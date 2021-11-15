class Contatto:
    
    def __init__(self, n, c, t, e):
        self.nome = n
        self.cognome = c
        self.telefono = t
        self.email = e

    def __init__(self):
        pass

    def get_nome(self):
        return self.nome

    def set_nome(self, n):
        self.nome = n

    def get_cognome(self):
        return self.cognome

    def set_cognome(self, c):
        self.cognome = c

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, t):
        self.telefono = t

    def get_email(self):
        return self.email

    def set_email(self, e):
        self.email = e

    def ToString(self):
        return "Nome: " + self.nome + "\nCognome: " + self.cognome + "\nTelefono: " + self.telefono + "\nEmail: " + self.email