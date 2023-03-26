# coding: utf-8
class Product:
    date = '2023-03-01'
    def __init__(self, name):
        self.name = name
    @classmethod
    def create_without_name(cls):
        return cls('')
    def change_date(self, date):
        self.date = date
        
p3 = Product('Feijão')
p3.change_date('2023-03-26')
p3.date
Product.date
