
MILEAGE = '0'


class Car:
    def __init__(self, producent: str, make: str, consuption: float, year=2020):
        self.year = year
        self.producent = producent.title()
        self.make = make.title()
        self.mileage = MILEAGE
        self.consuption = consuption

    def __str__(self) -> str:
        return f"{self.year} {self.producent} {self.make} - Mileage: {self.mileage} km, Consumption: {self.consuption} liters/100 km"

    def honk(self):
        return "Beep, beep!"

car1 = Car(producent="Toyota", make="Camry", consuption=8.5)
car2 = Car(producent="Honda", make="NSX", consuption=10.8)
car3 = Car(producent="Dodge", make="RAM", consuption=16.7)

print("Car 1:")
print(car1)
print("\nCar 2:")
print(car2)
print("\nCar 3:")
print(car3)

