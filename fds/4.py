# SE A 25 Shreyas Gangurde
# a) Write a Python program to store names and mobile numbers of your
# friends in sorted order on names. Search your friend from list using
# binary search (recursive and non- recursive). Insert friend if not
# present in phonebook

# b) Write a Python program to store names and mobile numbers of your
# friends in sorted order on names. Search your friend from list using
# Fibonacci search. Insert friend if not present in phonebook


def insert_entry(arr, name, number):

    for name_index in range(len(arr)):
        if name > arr[-1]:
            print(f'inserting {name} at end')
            arr.append(name)
            phonebookNumbers.append(number)
            break
        elif name > arr[name_index]:
            continue

        else:
            print(f'inserting {name} at {name_index}')
            arr.insert(name_index, name)
            phonebookNumbers.insert(name_index, number)
            break


def bin_rec_search(name, arr, start, end):
    print(start, end)
    mid = int((end-start)//2+start)

    if end < start:
        print("___NOT FOUND___")
        number = input(f"plz enter {name}'s phone number : ")
        insert_entry(arr, name, number)
        return -1

    if name == arr[mid]:
        print('Exactly mid')
        return mid
    elif name > arr[mid]:
        print('greater than mid')
        return bin_rec_search(name, arr, mid+1, end)
    elif name < arr[mid]:
        print('smaller than mid')
        return bin_rec_search(name, arr, start, mid-1)


def bin_ite_search(name, arr, start, end):
    # Not found block
    while start <= end:

        # print(start, end)
        mid = int((end-start)//2+start)
        if name == arr[mid]:
            return mid
        elif name < arr[mid]:
            end = mid - 1
        elif name > arr[mid]:
            start = mid + 1
    else:
        print("___NOT FOUND___")
        number = input(f"plz enter {name}'s phone number : ")
        insert_entry(arr, name, number)
        return -1


def fibonacci_search(name, arr):
    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2
    length = len(arr)
    while fib < length:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    offset = -1

    while fib > 1:

        i = min(fib2+offset, length-1)

        if arr[i] < name:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > name:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i
    if fib1 and arr[offset+1] == name:
        return offset + 1
    print("___NOT FOUND___")
    num = input(f"Enter {name}'s phone number : ")
    insert_entry(phonebookNames, name, num)
    return -1


#                   0           1       2       3       4       5           6       7       8       9
phonebookNames = ['Dinesh', 'Emily', 'Fred', 'Jack', 'Jonas', 'Kevin', 'Richard', 'Ron', 'Ross', 'Steve']
phonebookNumbers = ['9881251968', '9411111722', '9455667722', '9459999992', '9123888722', '9988551422', '9623103269', '9455667722', '8866442288', '7743882251']
print("""
        1) Binary Search Recursive
        2) Binary Search Iterative
        3) Fibonacci Search
        -1 for exit
        """)
while True:
    option = int(input("Choose an option : "))

    if option == 1:
        name = input("Enter the name you want to search : ")
        key = bin_rec_search(name, phonebookNames, 0, len(phonebookNames)-1)
        print("name found at : ", key)

    elif option == 2:
        name = input("Enter the name you want to search : ")
        key = bin_ite_search(name, phonebookNames, 0, len(phonebookNames) - 1)
        print("name found at : ", key)
    elif option == 3:
        name = input("Enter the name you want to search : ")
        key = fibonacci_search(name, phonebookNames)
        print("name found at : ", key)
    elif option == -1:
        break
