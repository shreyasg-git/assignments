'''

a)	Write a Python program to store names and mobile numbers of your friends in sorted order on names.
Search your friend from list using binary search (recursive and non- recursive).
Insert friend if not present in phonebook
b)	Write a Python program to store names and mobile numbers of your friends in sorted order on names.
Search your friend from list using Fibonacci search.
Insert friend if not present in phonebook.

'''


def BinarySearchRecursive(phonebook, low, high, num):
    global comparision_count
    if high < low:
        return False
    mid = low + ((high-low)//2)
    if num == phonebook[mid][1]:
        comparision_count += 1
        return True
    elif num < phonebook[mid][1]:
        comparision_count += 1
        return BinarySearchRecursive(phonebook, low, mid-1, num)
    else:
        comparision_count += 1
        return BinarySearchRecursive(phonebook, mid+1, high, num)


def BinarySearchIterative(phonebook, low, high, num):
    global comparision_count
    while low <= high:
        mid = low + ((high-low)//2)
        if num == phonebook[mid][1]:
            comparision_count += 1
            return True
        elif num < phonebook[mid][1]:
            comparision_count += 1
            high = mid-1
        else:
            comparision_count += 1
            low = mid+1
    return False


def FibonacciSearch(phonebook, num):
    global comparision_count
    M2 = 0
    M1 = 1
    M = M1 + M2
    n = len(phonebook)
    while M < n:
        M2 = M1
        M1 = M
        M = M1 + M2

    offset = -1

    while M > 1:

        i = min(M2+offset, n-1)

        if phonebook[i][1] < num:
            comparision_count += 1
            M = M1
            M1 = M2
            M2 = M - M1
            offset = i
        elif phonebook[i][1] > num:
            comparision_count += 1
            M = M2
            M1 = M1 - M2
            M2 = M - M1
        else:
            comparision_count += 1
            return True
    # Last elements as M1 can be 1 we are comming out of while loop at M1 == 1 and
    # that exact element is the element we are trying to find
    if(M1 and offset+1 < n):
        if(phonebook[offset+1][1] == num):
            comparision_count += 1
            return True

    return False


phonebook = []
comparision_count = 0

print("Choose how to search: ")
print("1) Input friends.")
print("2) Binary Search recursively.")
print("3) Binary Search non-recursively.")
print("4) Fibonacci search (PRACTICE PROBLEM)")

while(True):
    option = int(input("Menu Option: "))

    if option == 1:
        n = int(input("How many friends you want to add: "))
        for _ in range(n):
            phonebook.append((input("Name: "), int(input("Phone Number: "))))
    elif option == 2:
        comparision_count = 0
        search_name = input("Name of friend you want to search: ")
        phone_number = int(input("Phone number of friend: "))
        phonebook.sort(key=lambda x: x[1])
        if BinarySearchRecursive(phonebook, 0, len(phonebook)-1, phone_number):
            print(search_name, "is found in phonebook")
            print("Comparisions required:", comparision_count)
        else:
            print("Friend not found in phonebook.")
            print("Comparisions required:", comparision_count)
            print("Adding to phonebook.")
            phonebook.append((search_name, phone_number))
            phonebook.sort(key=lambda x: x[1])
            print("Phonebook now is ", phonebook)
    elif option == 3:
        comparision_count = 0
        search_name = input("Name of friend you want to search: ")
        phone_number = int(input("Phone number of friend: "))
        phonebook.sort(key=lambda x: x[1])
        if BinarySearchIterative(phonebook, 0, len(phonebook)-1, phone_number):
            print(search_name, "is found in phonebook")
            print("Comparisions required:", comparision_count)
        else:
            print("Friend not found in phonebook.")
            print("Comparisions required:", comparision_count)
            print("Adding to phonebook.")
            phonebook.append((search_name, phone_number))
            phonebook.sort(key=lambda x: x[1])
            print("Phonebook now is ", phonebook)
    elif option == 4:
        comparision_count = 0
        search_name = input("Name of friend you want to search: ")
        phone_number = int(input("Phone number of friend: "))
        phonebook.sort(key=lambda x: x[1])
        if FibonacciSearch(phonebook, phone_number):
            print(search_name, "is found in phonebook")
            print("Comparisions required:", comparision_count)
        else:
            print("Friend not found in phonebook.")
            print("Comparisions required:", comparision_count)
            print("Adding to phonebook.")
            phonebook.append((search_name, phone_number))
            phonebook.sort(key=lambda x: x[1])
            print("Phonebook now is ", phonebook)
    elif option == -1:
        break
    else:
        print('Invalid Input')

'''
Output

-------------------------
Test Case 1
6 8 23 21 13 70 34 16 2
key = 23
-------------------------

Choose how to search:
1) Input friends.
2) Binary Search recursively.
3) Binary Search non-recursively.
4) Fibonacci search (PRACTICE PROBLEM)
Menu Option: 1
How many friends you want to add: 9
Name: a
Phone Number: 6
Name: b
Phone Number: 8
Name: c
Phone Number: 23
Name: d
Phone Number: 21
Name: e
Phone Number: 13
Name: f
Phone Number: 70
Name: g
Phone Number: 34
Name: h
Phone Number: 16
Name: i
Phone Number: 2
Menu Option: 2
Name of friend you want to search: c
Phone number of friend: 23
c is found in phonebook 
Comparisions required: 2
Menu Option: 3
Name of friend you want to search: c
Phone number of friend: 23
c is found in phonebook 
Comparisions required: 2
Menu Option: 4
Name of friend you want to search: c
Phone number of friend: 23
c is found in phonebook
Comparisions required: 4
Menu Option: -1

-------------------------
Test Case 1
6 8 23 21 13 70 34 16 2
key = 99
-------------------------

# Result for recursive binary search

Choose how to search:
1) Input friends.
2) Binary Search recursively.
3) Binary Search non-recursively.
4) Fibonacci search (PRACTICE PROBLEM)
Menu Option: 1
How many friends you want to add: 9
Name: a
Phone Number: 6
Name: b
Phone Number: 8
Name: c
Phone Number: 23
Name: d
Phone Number: 21
Name: e
Phone Number: 13
Name: f
Phone Number: 70
Name: g
Phone Number: 34
Name: h
Phone Number: 16
Name: i
Phone Number: 2
Menu Option: 2
Name of friend you want to search: j
Phone number of friend: 99
Friend not found in phonebook.
Comparisions required: 4
Adding to phonebook.
Phonebook now is  [('i', 2), ('a', 6), ('b', 8), ('e', 13), ('h', 16), ('d', 21), ('c', 23), ('g', 34), ('f', 70), ('j', 99)]
Menu Option: -1

# Result for non recursive binary search

Choose how to search:
1) Input friends.
2) Binary Search recursively.
3) Binary Search non-recursively.
4) Fibonacci search (PRACTICE PROBLEM)
Menu Option: 1
How many friends you want to add: 9
Name: a
Phone Number: 6
Name: b
Phone Number: 8
Name: c
Phone Number: 23
Name: d
Phone Number: 21
Name: e
Phone Number: 13
Name: f
Phone Number: 70
Name: g
Phone Number: 34
Name: h
Phone Number: 16
Name: i
Phone Number: 2
Menu Option: 3
Name of friend you want to search: j
Phone number of friend: 99
Friend not found in phonebook.
Comparisions required: 4
Adding to phonebook.
Phonebook now is  [('i', 2), ('a', 6), ('b', 8), ('e', 13), ('h', 16), ('d', 21), ('c', 23), ('g', 34), ('f', 70), ('j', 99)]
Menu Option: -1


# Result for Fibonnaci Search (PRACTICE PROBLEM)
Choose how to search:
1) Input friends.
2) Binary Search recursively.
3) Binary Search non-recursively.
4) Fibonacci search (PRACTICE PROBLEM)
Menu Option: 1
How many friends you want to add: 9
Name: a
Phone Number: 6
Name: b
Phone Number: 8
Name: c
Phone Number: 23
Name: d
Phone Number: 21
Name: e
Phone Number: 13
Name: f
Phone Number: 70
Name: g
Phone Number: 34
Name: h
Phone Number: 16
Name: i
Phone Number: 2
Menu Option: 4
Name of friend you want to search: j
Phone number of friend: 99
Friend not found in phonebook.
Comparisions required: 5
Adding to phonebook.
Phonebook now is  [('i', 2), ('a', 6), ('b', 8), ('e', 13), ('h', 16), ('d', 21), ('c', 23), ('g', 34), ('f', 70), ('j', 99)]
Menu Option: -1

-------------------------
Test Case 2
1 2 3 4 5 6 7 8 9 10
key = 2
-------------------------

Choose how to search:
1) Input friends.
2) Binary Search recursively.
3) Binary Search non-recursively.
4) Fibonacci search (PRACTICE PROBLEM)
Menu Option: 1
How many friends you want to add: 10
Name: a
Phone Number: 1
Name: b
Phone Number: 2
Name: c
Phone Number: 3
Name: d
Phone Number: 4
Name: e
Phone Number: 5
Name: f
Phone Number: 6
Name: g
Phone Number: 7
Name: h
Phone Number: 8
Name: i
Phone Number: 9
Name: j
Phone Number: 10
Menu Option: 2
Name of friend you want to search: b
Phone number of friend: 2
b is found in phonebook 
Comparisions required: 2
Menu Option: 3
Name of friend you want to search: b
Phone number of friend: 2
b is found in phonebook
Comparisions required: 2
Menu Option: 4
Name of friend you want to search: b
Phone number of friend: 2
b is found in phonebook
Comparisions required: 2
Menu Option: -1

-------------------------
Test Case 2
1 2 3 4 5 6 7 8 9 10
key = 15
-------------------------
# Recursive binary search
Choose how to search:
1) Input friends.
2) Binary Search recursively.
3) Binary Search non-recursively.
4) Fibonacci search (PRACTICE PROBLEM)
Menu Option: 1
How many friends you want to add: 10
Name: a
Phone Number: 1
Name: b
Phone Number: 2
Name: c
Phone Number: 3
Name: d
Phone Number: 4
Name: e
Phone Number: 5
Name: f
Phone Number: 6
Name: g
Phone Number: 7
Name: h
Phone Number: 8
Name: i
Phone Number: 9
Name: j
Phone Number: 10
Menu Option: 2
Name of friend you want to search: k
Phone number of friend: 15
Friend not found in phonebook.
Comparisions required: 4
Adding to phonebook.
Phonebook now is  [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7), ('h', 8), ('i', 9), ('j', 10), ('k', 15)]
Menu Option: -1

# Non Recursive Binary search
Choose how to search:
1) Input friends.
2) Binary Search recursively.
3) Binary Search non-recursively.
4) Fibonacci search (PRACTICE PROBLEM)
Menu Option: 1
How many friends you want to add: 10
Name: a
Phone Number: 1
Name: b
Phone Number: 2
Name: c
Phone Number: 3
Name: d
Phone Number: 4
Name: e
Phone Number: 5
Name: f
Phone Number: 6
Name: g
Phone Number: 7
Name: h
Phone Number: 8
Name: i
Phone Number: 9
Name: j
Phone Number: 10
Menu Option: 2
Name of friend you want to search: k
Phone number of friend: 15
Friend not found in phonebook.
Comparisions required: 4
Adding to phonebook.
Phonebook now is  [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7), ('h', 8), ('i', 9), ('j', 10), ('k', 15)]
Menu Option: -1

# Fibonacci search
Choose how to search:
1) Input friends.
2) Binary Search recursively.
3) Binary Search non-recursively.     
4) Fibonacci search (PRACTICE PROBLEM)
Menu Option: 1
How many friends you want to add: 10
Name: a
Phone Number: 1
Name: b
Phone Number: 2
Name: c
Phone Number: 3
Name: d
Phone Number: 4
Name: e
Phone Number: 5
Name: f
Phone Number: 6
Name: g
Phone Number: 7
Name: h
Phone Number: 8
Name: i
Phone Number: 9
Name: j
Phone Number: 10
Menu Option: 4
Name of friend you want to search: k
Phone number of friend: 15
Friend not found in phonebook.
Comparisions required: 5
Adding to phonebook.
Phonebook now is  [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7), ('h', 8), ('i', 9), ('j', 10), ('k', 15)]
Menu Option: -1

-------------------------
Test Case 2
1 2 3 4 5 6 7 8 9 10
key = 9
-------------------------
Choose how to search:
1) Input friends.
2) Binary Search recursively.
3) Binary Search non-recursively.
4) Fibonacci search (PRACTICE PROBLEM)
Menu Option: 1
How many friends you want to add: 10
Name: a
Phone Number: 1
Name: b
Phone Number: 2
Name: c
Phone Number: 3
Name: d
Phone Number: 4
Name: e
Phone Number: 5
Name: f
Phone Number: 6
Name: g
Phone Number: 7
Name: h
Phone Number: 8
Name: i
Phone Number: 9
Name: j
Phone Number: 10
Menu Option: 2
Name of friend you want to search: i
Phone number of friend: 9
i is found in phonebook 
Comparisions required: 3
Menu Option: 3
Name of friend you want to search: i
Phone number of friend: 9
i is found in phonebook
Comparisions required: 3
Menu Option: 4
Name of friend you want to search: i
Phone number of friend: 9
i is found in phonebook
Comparisions required: 4
Menu Option: -1

-------------------------
Test Case 2
1 2 3 4 5 6 7 8 9 10
key = 5
-------------------------
Choose how to search:
1) Input friends.
2) Binary Search recursively.
3) Binary Search non-recursively.
4) Fibonacci search (PRACTICE PROBLEM)
Menu Option: 1
How many friends you want to add: 10
Name: a
Phone Number: 1
Name: b
Phone Number: 2
Name: c
Phone Number: 3
Name: d
Phone Number: 4
Name: e
Phone Number: 5
Name: f
Phone Number: 6
Name: g
Phone Number: 7
Name: h
Phone Number: 8
Name: i
Phone Number: 9
Name: j
Phone Number: 10
Menu Option: 2
Name of friend you want to search: e
Phone number of friend: 5
e is found in phonebook 
Comparisions required: 1
Menu Option: 3
Name of friend you want to search: e
Phone number of friend: 5
e is found in phonebook
Comparisions required: 1
Menu Option: 4
Name of friend you want to search: e
Phone number of friend: 5
e is found in phonebook
Comparisions required: 1
Menu Option: -1
'''
