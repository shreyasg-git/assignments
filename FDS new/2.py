'''
Write a Python program to compute following operations on String:
a)	To display word with the longest length
b)	To determines the frequency of occurrence of particular character in the string
c)	To check whether given string is palindrome or not
d)	To display index of first appearance of the substring
e)	To count the occurrences of each word in a given string
'''


def findStringLength(s):
    counter = 0
    for _ in s:
        counter += 1
    return counter


def findLongestString(strings, length):
    longest = strings[0]
    for i in range(1, length):
        if len(strings[i]) > len(longest):
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


def capitalizedName(string):
    string_list = string.split()
    newString = ""
    for word in string_list:
        newString += word.capitalize()+" "
    return newString


print("Chose a option from menu:")
print("1) To display word with the longest length")
print("2) To determines the frequency of occurrence of particular character in the string")
print("3) To check whether given string is palindrome or not")
print("4) To display index of first appearance of the substring")
print("5) To count the occurrences of each word in a given string")
print("6) Capitalize first letter of name (PRACTICE PROBLEM)")


while (True):
    option = int(input("Menu Option: "))

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
    elif option == 6:
        string = input("What is the name you want to capitalize: ")
        print("Capitalized form is", capitalizedName(string))
    elif option == -1:
        break
    else:
        print("Invalid Input")


'''
Output

Chose a option from menu:
1) To display word with the longest length
2) To determines the frequency of occurrence of particular character in the string
3) To check whether given string is palindrome or not
4) To display index of first appearance of the substring
5) To count the occurrences of each word in a given string
6) Capitalize first letter of name (PRACTICE PROBLEM)
Menu Option: 1
How many strings you want: 3
Input string: abcdef
Input string: xyz
Input string: lm
abcdef
Menu Option: 2
What is the string: nitin 
Character you want to find: i
2
Menu Option: 3
Input string you want to check: nitin
The string is a palindrome.
Menu Option: 3
Input string you want to check: asdfgh
The string is not a palindrome.
Menu Option: 4
What is the string: kkwaghkkwagh
What is the sub-string: wagh
Sub-string exists at location 2
Menu Option: 5
What is the string: kkwaghkkwaghkkwaghcollege
Which word you want to count: wagh
3
Menu Option: 6
What is the name you want to capitalize: sangeeta dinesh patil
Capitalized form is Sangeeta Dinesh Patil
Menu Option: -1
'''
