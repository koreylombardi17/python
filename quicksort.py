# Quicksort algorithm

from random import randrange 

def quicksort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[len(arr) // 2]
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	return quicksort(left) + middle + quicksort(right)

randomNumbers = []
for x in range(20):
	randomNumber = randrange(100)
	randomNumbers += [randomNumber]

print("Before quicksort:")
print(randomNumbers)
print("After quicksort:")
randomNumbers = quicksort(randomNumbers)
print(randomNumbers)
