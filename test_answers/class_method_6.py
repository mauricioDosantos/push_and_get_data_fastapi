# coding: utf-8
class Product:
    date = '2023-03-01'
    def __init__(self, name):
        self.name = name
    @classmethod
    def create_without_name(cls):
        return cls('')
        
Product.date
p = Product('Arroz')
p.date = '2023-03-26'
Product.date
p.date
p2 = Product.create_without_name()
p2.name
p2.date
