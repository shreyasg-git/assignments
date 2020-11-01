'''
Shreyas Balasaheb Gangurde
SE A 25
Write a Python program to compute following operations on String:
a)	To display word with the longest length
b)	To determines the frequency of occurrence of particular character in the string
c)	To check whether given string is palindrome or not
d)	To display index of first appearance of the substring
e)	To count the occurrences of each word in a given string
'''


def compute_string_length(s):
    counter = 0
    for _ in s:
        counter += 1
    return counter


def findLongestString(strings, length):
    longest = strings[0]
    for i in range(1, length):
        if compute_string_length(strings[i]) > compute_string_length(longest):
            longest = strings[i]
    return longest


def findCharacterInString(character, string):
    count = 0
    for i in string:
        if i == character:
            count += 1
    return count


def checkPalindrome(string):
    reversed = string[::-1]
    if string == reversed:
        return True
    return False


def checkSubString(string, subString):
    try:
        val = string.index(subString)
        return val
    except:
        return -1


def countWord(string, word):
    return string.count(word)


print("Chose a option from menu:")
print("1) To display word with the longest length")
print("2) To determines the frequency of occurrence of particular character in the string")
print("3) To check whether given string is palindrome or not")
print("4) To display index of first appearance of the substring")
print("5) To count the occurrences of each word in a given string")

option = int(input())

if option == 1:
    strings = []
    noOfStrings = int(input("How many strings you want: "))
    for _ in range(noOfStrings):
        strings.append(input("Input string: "))
    print(findLongestString(strings, noOfStrings))
elif option == 2:
    string = input("What is the string: ")
    character = input("Character you want to find: ")
    print(findCharacterInString(character, string))
elif option == 3:
    string = input("Input string you want to check: ")
    print("The string", "is" if checkPalindrome(
        string) else "is not", "a palindrome.")
elif option == 4:
    string = input("What is the string: ")
    subString = input("What is the sub-string: ")
    idx = checkSubString(string, subString)
    if idx == -1:
        print("Sub-string does not exist.")
    else:
        print("Sub-string exists at location", idx)
elif option == 5:
    string = input("What is the string: ")
    word = input("Which word you want to count: ")
    print(countWord(string, word))
else:
    print("Invalid Input")