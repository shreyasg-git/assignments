'''

Write a Python program to store second year percentage of
students in array. Write function for sorting array of 
floating point numbers in ascending order using
a)	Insertion sort
b)	Shell Sort and display top five scores

'''

import random


def InsertionSort(a):
    for i in range(1, len(a)):
        key = a[i]

        j = i-1
        while j >= 0 and key > a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key


def ShellSort(a):
    n = len(a)
    gap = n//2

    while gap > 1:
        for i in range(gap, n):

            temp = a[i]
            j = i
            while j >= gap and a[j-gap] < temp:
                a[j] = a[j-gap]
                j -= gap

            a[j] = temp
        gap //= 2


def QuickSort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)

    a[l], a[k] = a[k], a[l]
    m = partition2(a, l, r)
    QuickSort(a, l, m - 1)
    QuickSort(a, m + 1, r)


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] >= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


score = []
n = int(input("How many score: "))
for _ in range(n):
    score.append(float(input("Input Score: ")))

print("Choose which sort to use :- ")
print("1) Insertion Sort")
print("2) Shell Sort")
print("3) Quick Sort (PRACTICE PROBLEM)")

while(True):
    option = int(input("Menu Option: "))

    if (option == 1):
        InsertionSort(score)
        print("Top 5 score are", score[:5])
    elif (option == 2):
        ShellSort(score)
        print("Top 5 score are", score[:5])
    elif option == 3:
        QuickSort(score, 0, len(score)-1)
        print("Top 5 score are", score[:5])
    elif option == -1:
        break
    else:
        print("Invalid Input")

'''
Output

------------
Test Case 1
20 30 10 5 62 81 9
------------

How many score: 7
Input Score: 20
Input Score: 30
Input Score: 10
Input Score: 5
Input Score: 62
Input Score: 81
Input Score: 9
Choose which sort to use :-     
1) Insertion Sort
2) Shell Sort
3) Quick Sort (PRACTICE PROBLEM)
Menu Option: 1
Top 5 score are [81.0, 62.0, 30.0, 20.0, 10.0]
Menu Option: 2
Top 5 score are [81.0, 62.0, 30.0, 20.0, 10.0]
Menu Option: 3
Top 5 score are [81.0, 62.0, 30.0, 20.0, 10.0]
Menu Option: -1

------------
Test Case 2
5 7 8 15 20 56 67 10
------------
How many score: 8
Input Score: 5
Input Score: 7
Input Score: 8
Input Score: 15
Input Score: 20
Input Score: 56
Input Score: 67
Input Score: 10
Choose which sort to use :- 
1) Insertion Sort
2) Shell Sort
3) Quick Sort (PRACTICE PROBLEM)
Menu Option: 1
Top 5 score are [67.0, 56.0, 20.0, 15.0, 10.0]
Menu Option: 2
Top 5 score are [67.0, 56.0, 20.0, 15.0, 10.0]
Menu Option: 3
Top 5 score are [67.0, 56.0, 20.0, 15.0, 10.0]
Menu Option: -1

------------
Test Case 3
78 34 78 20 34 67 20 20 78 21 22
------------

How many score: 11
Input Score: 78
Input Score: 34
Input Score: 78
Input Score: 20
Input Score: 34
Input Score: 67
Input Score: 20
Input Score: 20
Input Score: 78
Input Score: 21
Input Score: 22
Choose which sort to use :-     
1) Insertion Sort
2) Shell Sort
3) Quick Sort (PRACTICE PROBLEM)
Menu Option: 1
Top 5 score are [78.0, 78.0, 78.0, 67.0, 34.0]
Menu Option: 2
Top 5 score are [78.0, 78.0, 78.0, 67.0, 34.0]
Menu Option: 3
Top 5 score are [78.0, 78.0, 78.0, 67.0, 34.0]
Menu Option: -1
'''
