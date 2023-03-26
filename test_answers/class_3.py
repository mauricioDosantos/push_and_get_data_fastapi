# coding: utf-8
class Client:
    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf
        
client_1 = Client('Alguém', '000.000.000-00')
print(client_1, client_1.name, client_1.cpf)
