'''
Assignment 1
Write a Python program to store marks scored in subject “Fundamental of Data Structure” 
by N students in the class. Write functions to compute following:
a)	The average score of class
b)	Highest score and lowest score of class
c)	Count of students who were absent for the test
d)	Display mark with highest frequency	

'''


def find_total(marks):
    total = 0
    for mark in marks:
        if mark != -1:
            total += mark
    return total


def find_average(marks, absent):
    t = find_total(marks)

    # considering absent
    if absent:
        try:
            return t / n
        except:
            return 0
    # not considering absent
    else:
        try:
            return t / (n - find_absent_student(marks))
        except:
            return 0


def find_min(marks):
    minimum = None
    for mark in marks:
        if mark != -1:
            if minimum == None:
                minimum = mark
            elif mark < minimum:
                minimum = mark

    return minimum


def find_max(marks):
    maximum = None
    for mark in marks:
        if mark != -1:
            if maximum == None:
                maximum = mark
            elif mark > maximum:
                maximum = mark

    return maximum


def print_marks(marks):
    print("Marks: ")
    for mark in marks:
        print(mark)


def find_highest_frequency(marks):
    number = []
    frequency = []

    # Setting frequency of each number
    for mark in marks:
        if mark != -1:
            if mark not in number:
                number.append(mark)
                frequency.append(1)
            else:
                index = number.index(mark)
                frequency[index] += 1

    # Finding marks with highest frequency
    maximum_index = None
    for i in range(len(frequency)):
        if maximum_index == None:
            maximum_index = i
        elif frequency[i] > frequency[maximum_index]:
            maximum_index = i
    try:
        return number[maximum_index]
    except:
        return None


def find_no_student_with_first_class(marks):
    number = []
    frequency = []

    # Setting frequency of each number
    for mark in marks:
        if mark != -1:
            if mark not in number:
                number.append(mark)
                frequency.append(1)
            else:
                index = number.index(mark)
                frequency[index] += 1

    no_of_first_class_students = 0
    for i in range(0, len(number)):
        if number[i] >= 90:
            no_of_first_class_students += frequency[i]

    return no_of_first_class_students


def find_absent_student(marks):
    no_absent = 0
    for mark in marks:
        if mark == -1:
            no_absent += 1

    return no_absent

# MAIN CODE


n = int(input("Number of students: "))
# displaying menu

marks = []
for _ in range(n):
    marks.append(int(input("Input marks: ")))

print("Menu")
print("1) Average considering absent students")
print("2) Average not considering absent students")
print("3) Maximum marks")
print("4) Minimum marks")
print("5) Absent Students")
print("6) Marks with highest frequency")
print("7) Number of students with first class in subject (PRACTICE PROBLEM)")
print("8) Print all marks")

while True:
    option = int(input("Enter menu option you want: "))

    if option == 1:
        print("Average considering absent student", find_average(marks, True))
    elif option == 2:
        print("Average not considering absent student",
              find_average(marks, False))
    elif option == 3:
        print("Maximum marks", find_max(marks))
    elif option == 4:
        print("Minimum marks", find_min(marks))
    elif option == 5:
        print("Absent students are", find_absent_student(marks))
    elif option == 6:
        print("Marks with highest frequency", find_highest_frequency(marks))
    elif option == 7:
        print("Number of first class students are",
              find_no_student_with_first_class(marks))
    elif option == 8:
        print_marks(marks)
    elif option == -1:
        break
    else:
        print("Invalid option")


'''
Output 

----------------------

Test Case 1
n = 6
10 20 -1 18 -1 -1

Output :
Number of students: 6
Input marks: 10
Input marks: 20
Input marks: -1
Input marks: 18
Input marks: -1
Input marks: -1
Menu
1) Average considering absent students
2) Average not considering absent students
3) Maximum marks
4) Minimum marks
5) Absent Students
6) Marks with highest frequency
7) Number of students with first class in subject (PRACTICE PROBLEM)
8) Print all marks
Enter menu option you want: 1
Average considering absent student 8.0
Enter menu option you want: 2
Average not considering absent student 16.0
Enter menu option you want: 3
Maximum marks 20
Enter menu option you want: 4
Minimum marks 10
Enter menu option you want: 5
Absent students are 3       
Enter menu option you want: 6
Marks with highest frequency 10
Enter menu option you want: 7  
Number of first class students are 0
Enter menu option you want: 8
Marks: 
10
20
-1
18
-1
-1
Enter menu option you want: -1

----------------------

Test Case 2
n = 6
-1 20 -1 18 -1 15

Output :
Number of students: 6
Input marks: -1
Input marks: 20
Input marks: -1
Input marks: 18
Input marks: -1
Input marks: 15
Menu
1) Average considering absent students
2) Average not considering absent students
3) Maximum marks
4) Minimum marks
5) Absent Students
6) Marks with highest frequency
7) Number of students with first class in subject (PRACTICE PROBLEM)
8) Print all marks
Enter menu option you want: 1
Average considering absent student 8.833333333333334
Enter menu option you want: 2
Average not considering absent student 17.666666666666668
Enter menu option you want: 3
Maximum marks 20
Enter menu option you want: 4
Minimum marks 15
Enter menu option you want: 5
Absent students are 3
Enter menu option you want: 6
Marks with highest frequency 20
Enter menu option you want: 7
Number of first class students are 0
Enter menu option you want: 8
Marks: 
-1
20
-1
18
-1
15
Enter menu option you want: -1

----------------------

Test Case 3
n = 7
-1 -1 -1 -1 -1 -1 -1

Output : 
Number of students: 7
Input marks: -1
Input marks: -1
Input marks: -1
Input marks: -1
Input marks: -1
Input marks: -1
Input marks: -1
Menu
1) Average considering absent students
2) Average not considering absent students
3) Maximum marks
4) Minimum marks
5) Absent Students
6) Marks with highest frequency
7) Number of students with first class in subject (PRACTICE PROBLEM)
8) Print all marks
Enter menu option you want: 1
Average considering absent student 0.0
Enter menu option you want: 2
Average not considering absent student 0
Enter menu option you want: 3
Maximum marks None
Enter menu option you want: 4
Minimum marks None
Enter menu option you want: 5
Absent students are 7
Enter menu option you want: 6
Marks with highest frequency None
Enter menu option you want: 7
Number of first class students are 0
Enter menu option you want: 8
Marks: 
-1
-1
-1
-1
-1
-1
-1
Enter menu option you want: -1
'''
