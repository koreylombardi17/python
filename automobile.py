# Program to learn class creation and inheritance syntax in python

class Automobile:
	def __init__(self, name, year, gas_mileage):
		self.name = name
		self.year = year
		self.gas_mileage = gas_mileage

	def __str__(self):
		return ("Name: " + self.name 
			+ "\nYear: " + str(self.year) 
			+ "\nGas Mileage: " + str(self.gas_mileage))

class Car(Automobile):
	def __init__(self, name, year, gas_mileage, number_doors):
		super().__init__(name, year, gas_mileage)
		self.number_doors = number_doors

	def __str__(self):
		return (super().__str__() 
			+ "\nNumber of doors: " + str(self.number_doors))

class Truck(Automobile):
	def __init__(self, name, year, gas_mileage, bed_type):
		super().__init__(name, year, gas_mileage)
		self.bed_type = bed_type

	def __str__(self):
		return (super().__str__() 
			+ "\nBed type: " + self.bed_type)


# Created Objects of different types
automobile = Automobile("Automobile", 2008, 28)
car = Car("Acura TL", 2008, 28, 4)
truck = Truck("Ford F-150", 2015, 20, "Crew")

print(automobile)
print()

print(car)
print()

print(truck)
