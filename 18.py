class Product:
    def __init__(self, price):
        self._price = price  

    
    @property
    def price(self):
        return self._price

    
    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self._price = new_price
        else:
            print("Price cannot be negative.")

    
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price


p = Product(100)

print("Price:", p.price)


p.price = 150
print("Updated Price:", p.price)


del p.price
