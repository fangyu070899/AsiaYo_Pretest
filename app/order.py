"""
初始化 order 與其屬性
"""
class Order:
    def __init__(self, id, name, address, price, currency):
        self.id = id
        self.name = name
        self.address = address
        self.price = price
        self.currency = currency
