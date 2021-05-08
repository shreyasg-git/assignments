# Write a Python program to store second year percentage of students in array. 
# Write function for sorting array of floating point numbers in ascending order using
# a)	Insertion sort
# b)	Shell Sort and display top five scores

perc = list()
print("Enter Percentages one by one and enter -1 at end")
while True:
	per = float(input("Enter Percentage : "))
	if (per == -1):
		print("Input Process Complete")
		break
	perc.append(per)
print("main array is", perc)

def insertionSortAsc(arr):
	for i in range(len(arr)):
		key = arr[i]
		j = i
		while j > 0 and key < arr[j - 1]:
			arr[j] = arr[j - 1]
			j -= 1
			arr[j] = key
			print(arr)
			
# only < is changed to make it descending in `while j > 0 and key '>' arr[j - 1]:`
def insertionSortDesc(arr):
	for i in range(len(arr)):
		key = arr[i]
		j = i
		while j > 0 and key > arr[j - 1]:
			arr[j] = arr[j - 1]
			j -= 1
			arr[j] = key
			print(arr)

perc = [34, 32, 54, 65, 234 ,453, 78, 78, 78, 23, 54, 67, 67 ,32, 78, 34, 98, 90, 98, 98]
insertionSortDesc(perc)