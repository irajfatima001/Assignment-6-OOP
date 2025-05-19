class Car:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print(f"{self.brand} engine has started.")

car1 = Car("civic")
print(car1.brand)
car1.start_engine()