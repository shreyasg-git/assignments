# Write a Python program to store first year percentage of students in array.
# Write function for sorting array of floating point numbers in ascending order using
# a)	Selection Sort
# b)	Bubble sort and display top five scores.

perc = list()
print("Enter Percentages one by one and enter -1 at end")
while True:
    per = float(input("Enter Percentage : "))
    if (per == -1):
        print("Input Process Complete")
        break
    perc.append(per)
print("main array is", perc)


def findMin(arr):
    ind = 0
    min = arr[0]
    for i in range(len(arr)):
        if min > arr[i]:
            min = arr[i]
            ind = i
    return min, ind


def SelectionSortAsc(arr):
    i = 0
    # for i in range(len(arr)):
    while i < len(arr):
        # num = min(arr[i:])
        num, ind = findMin(arr[i:])
        print("num is", num)
        print("before", arr[i:])
        arr[i], arr[i+ind] = arr[i+ind], arr[i]
        print("after", arr[i:])
        print(arr)
        i += 1


def SelectionSortDesc(arr):
    i = 0
    while i < len(arr):
        num, ind = findMin(arr[i:])
        print("num is", num, "and index is ", ind)
        arr.pop(i+ind)
        arr.insert(0, num)
        i += 1
        print(arr)


def bubbleSortAsc(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)


def bubbleSortDesc(arr):

    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)


# SelectionSortAsc(perc)
# SelectionSortDesc(perc)
# bubbleSort(perc)
bubbleSortDesc(perc)
print(perc)
