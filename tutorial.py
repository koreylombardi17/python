# This is a tutorial python file 
# Performing simple tasks to get used to the language

import sys
from datetime import datetime

# Print name
print("Name printed out:")
print("Korey Lombardi")

# Print sentence with tabs and new lines
print("")
print("Print sentence with tabs and new lines:")
print("Korey Lombardi is 27.\n\tConnor Lombardi is 20\n\t\tKyle Lombardi is 30.")

# Print the current version of Python
print()
print("Python Version:")
print(sys.version)

# Print Python version info:
print()
print("Python Version info:")
print(sys.version_info)

# Write a for loop iterating through a list
print()
print("For loop iterating through a list:")
fruits = ["Apples", "Bananas", "Cherries"]
for x in fruits:
	print(x)

# Write a for loop iterating through a tuple
print()
print("For loop iterating through a tuple:")
fruits = ("Apples", "Bananas", "Cherries")
for x in fruits:
	print(x)

# Print out the current date and time
print()
print("Current date and time:")
print(datetime.now())

# Float division and int division(rounded 2 decimal places)
print()
a = 5
b = 3
print("Float division: a/b = " + str(round(a/b, 2)))
print("Int division: a/b = " + str(a//b))

# Basic for loop calculating i^2
print()
print("Basic for loop calculating i^2")
for i in range(10):
	print(str(i) + "*" + str(i) + "=" + str(i*i))

# Basic loop concatenating numbers to the end of a string without adding new lines after each iteration  
print()
print("Basic loop concatenating numbers to the end of a string without adding new lines after each iteration")
n = 10
for i in range(1, n+1):
	print(i, end='')
print()

# Funtion to calculate Gregorian calendar leap years
def is_leap(year):
	leap = False

	if(year < 1900):
		return False

	if(year % 400 == 0 and 
		year % 100 == 0 and
		year % 4 == 0):
		leap = True
	elif(year % 4 == 0 and
		year % 100 == 0):
		leap = False
	elif(year % 4 == 0):
		leap = True

	return leap

print()
print("Gregorian calendar: isLeap(1990) = " + str(is_leap(1990)))
