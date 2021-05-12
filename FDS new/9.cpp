/*

A palindrome is a string of character that‘s the same forward and backward. 
Typically, punctuation, capitalization, and spaces are ignored. 
For example, “Poor Dan is in a droop” is a palindrome, as can
be seen by examining the characters “poor danisina droop” and observing that
they are the same forward and backward. One way to check for a palindrome is to reverse the
characters in the string and then compare with them the original-in a palindrome,
the sequence will be identical. Write C++ program with functions-

a)	To print original string followed by reversed string using stack
b)	To check whether given string is palindrome or not
*/
#include <iostream>
#include <string>
using namespace std;

template <typename T>
class Stack
{
    struct Node
    {
        T value;
        Node *next;
    };
    Node *head;
    int length;

public:
    Stack()
    {
        head = NULL;
        length = 0;
    }
    void push(T new_val)
    {
        Node *new_head = new Node;
        new_head->value = new_val;
        new_head->next = head;
        head = new_head;
        length++;
    }

    T getTop()
    {
        return head->value;
    }

    void pop()
    {
        head = head->next;
        length--;
    }

    bool isEmpty()
    {
        return length == 0;
    }
};

string ReverseString(string s)
{
    Stack<char> ls;
    for (int i = 0; i < s.length(); i++)
    {
        if ((int)s[i] > 64 && (int)s[i] < 91)
        {
            ls.push((char)((int)s[i] + 32));
        }
        else if ((int)s[i] > 96 && (int)s[i] < 123)
        {
            ls.push(s[i]);
        }
    }
    string rev_string;
    while (!ls.isEmpty())
    {
        rev_string += ls.getTop();
        ls.pop();
    }
    return rev_string;
}

bool CheckPalindrome(string s)
{
    string reverse_string = ReverseString(s);
    string original_string = ReverseString(reverse_string);
    cout << "Original string " << original_string << endl;
    cout << "Reversed string " << reverse_string << endl;
    if (original_string == reverse_string)
        return true;
    else
        return false;
}

void findBinary(int num)
{
    Stack<int> binary;
    while (num != 0)
    {
        //cout << num % 2 << endl;
        binary.push(num % 2);
        num = num / 2;
    }
    while (!binary.isEmpty())
    {
        cout << (char)(binary.getTop() + 48);
        binary.pop();
    }
    cout << endl;
}

int main(void)
{
    cout << "Menu" << endl;
    cout << "1) Input String" << endl;
    cout << "2) Check Palindrome" << endl;
    cout << "3) Decimal to Binary(PRACTICE PROBLEM)" << endl;
    int option;
    bool breakFlag = false;
    string inp = "";
    while (!breakFlag)
    {
        cout << "Menu Option: ";
        cin >> option;
        switch (option)
        {
        case 1:
            cout << "String Input: ";
            cin.ignore();
            getline(cin, inp);
            break;
        case 2:
            if (CheckPalindrome(inp))
                cout << "String is Palindrome" << endl;
            else
                cout << "String is not Palindrome" << endl;
            break;
        case 3:
            int decimal;
            cout << "Input Decimal number: ";
            cin >> decimal;
            findBinary(decimal);
            break;
        case -1:
            breakFlag = true;
            break;
        default:
            cout << "Invalid Input" << endl;
            break;
        }
    }
    return 0;
}

/*
Output

-------------------
Test Case 1
madam
-------------------

Menu
1) Input String
2) Check Palindrome
3) Decimal to Binary(PRACTICE PROBLEM)
Menu Option: 1
String Input: madam
Menu Option: 2
Original string madam
Reversed string madam
String is Palindrome 
Menu Option: -1

-------------------
Test Case 2
Madam
-------------------

Menu
1) Input String
2) Check Palindrome
3) Decimal to Binary(PRACTICE PROBLEM)
Menu Option: 1
String Input: Madam
Menu Option: 2
Original string madam
Reversed string madam
String is Palindrome 
Menu Option: -1

-------------------
Test Case 3
"Madam"
-------------------

Menu
1) Input String
2) Check Palindrome
3) Decimal to Binary(PRACTICE PROBLEM)
Menu Option: 1
String Input: "Madam"
Menu Option: 2
Original string madam
Reversed string madam
String is Palindrome 
Menu Option: -1

-------------------
Test Case 4
1.Poor Dan is in a droop!
-------------------

Menu
1) Input String
2) Check Palindrome
3) Decimal to Binary(PRACTICE PROBLEM)
Menu Option: 1
String Input: 1.Poor Dan is in a droop!
Menu Option: 2
Original string poordanisinadroop
Reversed string poordanisinadroop
String is Palindrome
Menu Option: -1

-------------------
Test Case 5
Convert 565 from decimal to Binary using stack
-------------------
Menu
1) Input String
2) Check Palindrome
3) Decimal to Binary(PRACTICE PROBLEM)
Menu Option: 3
Input Decimal number: 565
1000110101   
Menu Option: -1
*/