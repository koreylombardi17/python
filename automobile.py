# Program to learn class creation and inheritance syntax in python

class Automobile:
	def __init__(self, name, year, gas_mileage):
		self.name = name
		self.year = year
		self.gas_mileage = gas_mileage

class Car(Automobile):
	def __init__(self, name, year, gas_mileage, number_doors):
		super().__init__(name, year, gas_mileage)
		self.number_doors = number_doors

class Truck(Automobile):
	def __init__(self, name, year, gas_mileage, bed_type):
		super().__init__(name, year, gas_mileage)
		self.bed_type = bed_type

automobile = Automobile("Automobile", 2008, 28)
car = Car("Acura TL", 2008, 28, 4)
truck = Truck("Ford F-150", 2015, 20, "Crew")

print(automobile.name)
print(automobile.year)
print(automobile.gas_mileage)
print()

print(car.name)
print(car.year)
print(car.gas_mileage)
print(car.number_doors)
print()

print(truck.name)
print(truck.year)
print(truck.gas_mileage)
print(truck.bed_type)
