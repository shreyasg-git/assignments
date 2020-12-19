# SE A 25 Shreyas Gangurde
# Write a Python program to store marks scored in subject “Fundamental of Data Structure” by
# N students in the class. Write functions to compute following:
# a) The average score of class
# b) Highest score and lowest score of class
# c) Count of students who were absent for the test
# d) Display mark with highest frequency



def compute_average_score(arr):
    sum_of_marks = 0
    for i in range(len(arr)):
        if arr[i] != -1:
            sum_of_marks += arr[i]
    average = sum_of_marks/len(arr)
    return average


def compute_highest_and_lowest(arr):
    high_and_low = []

    def compute_highest(arr):
        highest = arr[0]
        for i in range(len(arr)):
            if arr[i] >= highest:
                highest = arr[i]
            else:
                continue
        return highest

    def compute_lowest(arr):
        lowest = 9999
        for i in range(len(arr)):
            if arr[i] <= lowest and arr[i] != -1:
                lowest = arr[i]
            else:
                continue
        return lowest

    high_and_low.append(compute_highest(arr))
    high_and_low.append(compute_lowest(arr))
    # print(highAndLow)
    return high_and_low


def compute_absent_count(arr):
    abs_count = 0
    for i in range(len(arr)):
        if arr[i] == -1:
            abs_count += 1
        else:
            continue

    return abs_count


def compute_highest_frequency(arr):
    marks_and_frequency = dict()
    for i in range(len(arr)):
        if str(arr[i]) not in marks_and_frequency:
            marks_and_frequency[f'{arr[i]}'] = 1
        else:
            marks_and_frequency[f'{arr[i]}'] += 1
    highest_freq = 0
    highest_freq_key = 0
    for j in marks_and_frequency:
        if marks_and_frequency[j] >= highest_freq:
            highest_freq = marks_and_frequency[j]
            highest_freq_key = j
    return highest_freq_key, highest_freq


n = int(input("Enter The Number of Students : "))
marksArray = []
for i in range(n):
    marks = int(input(f"Enter the marks of student number {i+1} : "))
    marksArray.append(marks)

print("Menu")
print("1) Average Marks")
print("2) Maximum And Minimum Marks")
print("3) Count of Absent Students")
print("4) Marks with highest frequency")
print("5) Print all marks")
print("-1 to exit")

while True:
    option = int(input("Enter menu option you want: "))

    if option == 1:
        print("Average marks are : ", compute_average_score(marksArray))
    elif option == 2:
        print("Maximum and Minimum marks are ", compute_highest_and_lowest(marksArray), 'respectively')
    elif option == 3:
        print("Absent students are", compute_absent_count(marksArray))
    elif option == 4:
        print(f'Marks with highest frequency is {compute_highest_frequency(marksArray)[0]} with frequency {compute_highest_frequency(marksArray)[1]}')
    elif option == 5:
        print(marksArray)
    elif option == -1:
        break
    else:
        print("Invalid option")

