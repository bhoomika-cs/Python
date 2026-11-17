#Create a Car class with attributes like brand and model. Then create an instance of this class.
class Car:
    def __init__(self, brand, model): 
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    def general_description(self):
         return "Cars are means of transport"
    
my_car = Car("Toyota", "Corolla")
print(my_car.get_brand())
#print(my_car.model)
print(my_car.full_name())

#inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
            return "Electric Charge"

my_tesla = ElectricCar("Tesla", "Model S", "85KWh")
# print(my_tesla.full_name())
# print(my_tesla.__brand)
print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())    #Polymorphism
print(safari.general_description())    #Polymorphism






