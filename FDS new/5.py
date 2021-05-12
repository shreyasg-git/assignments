'''

Write a Python program to store first year percentage of students in array.
Write function for sorting array of floating point numbers in ascending order using
a)	Selection Sort
b)	Bubble sort and display top five scores.

'''


def BubbleSort(a, reverse=False, sortBy="cgpa"):
    n = len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if reverse:
                if a[j].getVal(sortBy) < a[j+1].getVal(sortBy):
                    a[j], a[j+1] = a[j+1], a[j]
            else:
                if a[j].getVal(sortBy) > a[j+1].getVal(sortBy):
                    a[j], a[j+1] = a[j+1], a[j]


def SelectionSort(a, reverse=False, sortBy="cgpa"):
    n = len(a)
    for i in range(n):
        mid = i
        for j in range(i+1, n):
            if reverse:
                if (a[j].getVal(sortBy) > a[mid].getVal(sortBy)):
                    mid = j
            else:
                if (a[j].getVal(sortBy) < a[mid].getVal(sortBy)):
                    mid = j
        a[i], a[mid] = a[mid], a[i]


def displayStudents(arr, limit=-1):
    if limit > len(arr) or limit == -1:
        limit = len(arr)
    print("\t", end="")
    for i in range(0, limit):
        print("(", arr[i].name, ",", arr[i].cgpa, ")", end=", ")
    print("")


class student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def getVal(self, val):
        if(val == "name"):
            return self.name
        else:
            return self.cgpa


students = []
num = int(input("How may students: "))
for i in range(num):
    nm = input(f"Name of student {i+1}: ")
    score = float(input(f"CGPA of student {i+1}: "))
    students.append(student(nm, score))

print("Choose which sort to use :- ")
print("1) Selection Sort Top 5 scores")
print("2) Bubble Sort Top 5 Scores")
print("3) Sort By user choice (PRACTICE PROBLEM)")
while(True):
    option = int(input("Menu Option: "))

    if option == 1:
        SelectionSort(students, True)
        print("Top 5 score are")
        displayStudents(students, 5)
    elif option == 2:
        BubbleSort(students, True)
        print("Top 5 score are")
        displayStudents(students, 5)
    elif option == 3:
        print("Which Sort?")
        print("1) Selection Sort")
        print("2) Bubble Sort")
        sort_option = int(input("Option: "))
        print("Sort By?")
        print("1) Name")
        print("2) CGPA")
        sort_by_option = int(input("Option: "))
        print("Order By?")
        print("1) Ascending")
        print("2) Descending")
        order_option = int(input("Option: "))
        if(sort_option == 1 and sort_by_option == 1 and order_option == 1):
            SelectionSort(students, False, "name")
            displayStudents(students)
        elif(sort_option == 1 and sort_by_option == 1 and order_option == 2):
            SelectionSort(students, True, "name")
            displayStudents(students)
        elif(sort_option == 1 and sort_by_option == 2 and order_option == 1):
            SelectionSort(students, False, "cgpa")
            displayStudents(students)
        elif(sort_option == 1 and sort_by_option == 2 and order_option == 2):
            SelectionSort(students, True, "cgpa")
            displayStudents(students)
        elif(sort_option == 2 and sort_by_option == 1 and order_option == 1):
            BubbleSort(students, False, "name")
            displayStudents(students)
        elif(sort_option == 2 and sort_by_option == 1 and order_option == 2):
            BubbleSort(students, True, "name")
            displayStudents(students)
        elif(sort_option == 2 and sort_by_option == 2 and order_option == 1):
            BubbleSort(students, False, "cgpa")
            displayStudents(students)
        elif(sort_option == 2 and sort_by_option == 2 and order_option == 2):
            BubbleSort(students, True, "cgpa")
            displayStudents(students)
        else:
            print("There was an invalid input!")

    elif option == -1:
        break
    else:
        print("Invalid Input")

'''
Output

-----
Test Case 1
20 30 10 5 62 81 9
-----

How may students: 7
Name of student 1: a
CGPA of student 1: 20
Name of student 2: b
CGPA of student 2: 30
Name of student 3: c
CGPA of student 3: 10
Name of student 4: d
CGPA of student 4: 5
Name of student 5: e
CGPA of student 5: 62
Name of student 6: f
CGPA of student 6: 81
Name of student 7: g
CGPA of student 7: 9
Choose which sort to use :-
1) Selection Sort Top 5 scores
2) Bubble Sort Top 5 Scores
3) Sort By user choice (PRACTICE PROBLEM)
Menu Option: 1
Top 5 score are
        ( f , 81.0 ), ( e , 62.0 ), ( b , 30.0 ), ( a , 20.0 ), ( c , 10.0 ),
Menu Option: 2
Top 5 score are
        ( f , 81.0 ), ( e , 62.0 ), ( b , 30.0 ), ( a , 20.0 ), ( c , 10.0 ),
Menu Option: 3
Which Sort?
1) Selection Sort
2) Bubble Sort
Option: 1
Sort By?
1) Name
2) CGPA
Option: 1
Order By?
1) Asscending
2) Descending
Option: 1
        ( a , 20.0 ), ( b , 30.0 ), ( c , 10.0 ), ( d , 5.0 ), ( e , 62.0 ), ( f , 81.0 ), ( g , 9.0 ),
Menu Option: -1


-----
Test Case 2
5 7 8 15 20 56 67 10
-----

How may students: 8
Name of student 1: a
CGPA of student 1: 5
Name of student 2: b
CGPA of student 2: 7
Name of student 3: c
CGPA of student 3: 8
Name of student 4: d
CGPA of student 4: 15
Name of student 5: e
CGPA of student 5: 20
Name of student 6: f
CGPA of student 6: 56
Name of student 7: g
CGPA of student 7: 67
Name of student 8: h
CGPA of student 8: 10
Choose which sort to use :-
1) Selection Sort Top 5 scores
2) Bubble Sort Top 5 Scores
3) Sort By user choice (PRACTICE PROBLEM)
Menu Option: 1
Top 5 score are
        ( g , 67.0 ), ( f , 56.0 ), ( e , 20.0 ), ( d , 15.0 ), ( h , 10.0 ), 
Menu Option: 2
Top 5 score are
        ( g , 67.0 ), ( f , 56.0 ), ( e , 20.0 ), ( d , 15.0 ), ( h , 10.0 ), 
Menu Option: -1

-----
Test Case 3
78 34 78 20 34 67 20 20 78 21 22
-----

How may students: 11
Name of student 1: a
CGPA of student 1: 78
Name of student 2: b
CGPA of student 2: 34
Name of student 3: c
CGPA of student 3: 78
Name of student 4: d
CGPA of student 4: 20
Name of student 5: e
CGPA of student 5: 34
Name of student 6: f
CGPA of student 6: 67
Name of student 7: g
CGPA of student 7: 20
Name of student 8: h
CGPA of student 8: 20
Name of student 9: i
CGPA of student 9: 78
Name of student 10: j
CGPA of student 10: 21
Name of student 11: k
CGPA of student 11: 22
Choose which sort to use :-
1) Selection Sort Top 5 scores
2) Bubble Sort Top 5 Scores
3) Sort By user choice (PRACTICE PROBLEM)
Menu Option: 1
Top 5 score are
        ( a , 78.0 ), ( c , 78.0 ), ( i , 78.0 ), ( f , 67.0 ), ( e , 34.0 ),
Menu Option: 2
Top 5 score are
        ( a , 78.0 ), ( c , 78.0 ), ( i , 78.0 ), ( f , 67.0 ), ( e , 34.0 ),
Menu Option: 3
Which Sort?
1) Selection Sort
2) Bubble Sort
Option: 1
Sort By?
1) Name
2) CGPA
Option: 2
Order By?
1) Asscending
2) Descending
Option: 1
        ( d , 20.0 ), ( h , 20.0 ), ( g , 20.0 ), ( j , 21.0 ), ( k , 22.0 ), ( b , 34.0 ), ( e , 34.0 ), ( f , 67.0 ), ( a , 78.0 ), ( c , 78.0 ), ( i , 78.0 ),
Menu Option: -1

'''
