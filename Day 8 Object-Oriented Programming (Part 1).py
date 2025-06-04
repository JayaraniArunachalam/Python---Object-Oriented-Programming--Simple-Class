class Car:
    def __init__(self, brand, model, year, color,fuel):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.fuel = fuel

    def display(self):
        print("Car Details:")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Color:", self.color)
        print("Fuel Type:",self.fuel)

mycar = Car("Suzuki","Swift Dzire",2021,"Gold","Petrol")
mycar.display()