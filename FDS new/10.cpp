/*


Implement C++ program for expression conversion as infix 
to postfix and its evaluation using stack based on given conditions:
1.	Operands and operator, both must be single character.
2.	Input Postfix expression must be in a desired format.
Only '+', '-', '*' and '/ ' operators are expected.

*/

#include <iostream>
#include <string>
#include <math.h>
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

string ReverseString(string inp)
{
    string new_string = "";
    for (int i = inp.length() - 1; i >= 0; i--)
    {
        new_string += inp[i];
    }
    return new_string;
}

int CheckPrecedence(char incomingOperator, char operator2)
{
    // 0 if precedence is same
    // 1 if precedence of incoming operator is higher
    //-1 if precedence of incoming operator is lower
    switch (incomingOperator)
    {
    case '+':
        if (operator2 == '-' || operator2 == '+')
            return 0;
        else
            return -1;
    case '-':
        if (operator2 == '+' || operator2 == '-')
            return 0;
        else
            return -1;
    case '*':
        if (operator2 == '^')
            return -1;
        else if (operator2 == '/' || operator2 == '*')
            return 0;
        else
            return 1;
    case '/':
        if (operator2 == '^')
            return -1;
        else if (operator2 == '*' || operator2 == '/')
            return 0;
        else
            return 1;
    case '^':
        return 1;
    default:
        return -1;
    }
}

void InfixToPrefixOperatorLogic(char opp, Stack<char> &s, string &ans)
{
    if (!s.isEmpty())
    {
        if (s.getTop() == ')')
        {
            s.push(opp);
            return;
        }
        if (CheckPrecedence(opp, s.getTop()) == 1)
            s.push(opp);
        else if (CheckPrecedence(opp, s.getTop()) == -1)
        {
            while ((CheckPrecedence(opp, s.getTop()) == -1))
            {
                ans += s.getTop();
                s.pop();
                if (s.isEmpty())
                    break;
            }
            s.push(opp);
        }
        else
            s.push(opp);
    }
    else
        s.push(opp);
}

string InfixToPrefix(string exp)
{
    exp = ReverseString(exp);
    string ans = "";
    Stack<char> s;
    for (int i = 0; i < exp.length(); i++)
    {
        switch (exp[i])
        {
        case '+':
        {
            InfixToPrefixOperatorLogic('+', s, ans);
            break;
        }
        case '-':
        {
            InfixToPrefixOperatorLogic('-', s, ans);
            break;
        }
        case '*':
        {
            InfixToPrefixOperatorLogic('*', s, ans);
            break;
        }
        case '/':
        {
            InfixToPrefixOperatorLogic('/', s, ans);
            break;
        }
        case '^':
        {
            InfixToPrefixOperatorLogic('^', s, ans);
            break;
        }
        case '(':
        {
            while (s.getTop() != ')')
            {
                ans += s.getTop();
                s.pop();
            }
            s.pop();
            break;
        }
        case ')':
        {
            s.push(')');
            break;
        }
        default:
        {
            ans += exp[i];
            break;
        }
        };
    }
    while (!s.isEmpty())
    {
        ans += s.getTop();
        s.pop();
    }
    ans = ReverseString(ans);
    return ans;
}

void InfixToPostfixOperatorLogic(char opp, Stack<char> &s, string &ans)
{
    if (!s.isEmpty())
    {
        if (s.getTop() == '(')
        {
            s.push(opp);
            return;
        }
        if (CheckPrecedence(opp, s.getTop()) == 1)
            s.push(opp);
        else
        {
            while (CheckPrecedence(opp, s.getTop()) != 1 && s.getTop() != '(')
            {
                ans += s.getTop();
                s.pop();
                if (s.isEmpty())
                    break;
            }
            s.push(opp);
        }
    }
    else
        s.push(opp);
}

string InfixToPostfix(string exp)
{
    string ans = "";
    Stack<char> s;
    for (int i = 0; i < exp.length(); i++)
    {
        switch (exp[i])
        {
        case '+':
        {
            InfixToPostfixOperatorLogic('+', s, ans);
            break;
        }
        case '-':
        {
            InfixToPostfixOperatorLogic('-', s, ans);
            break;
        }
        case '*':
        {
            InfixToPostfixOperatorLogic('*', s, ans);
            break;
        }
        case '/':
        {
            InfixToPostfixOperatorLogic('/', s, ans);
            break;
        }
        case '^':
        {
            InfixToPostfixOperatorLogic('^', s, ans);
            break;
        }
        case ')':
        {
            while (s.getTop() != '(')
            {
                ans += s.getTop();
                s.pop();
            }
            s.pop();
            break;
        }
        case '(':
        {
            s.push('(');
            break;
        }
        default:
        {
            ans += exp[i];
            break;
        }
        };
    }
    while (!s.isEmpty())
    {
        ans += s.getTop();
        s.pop();
    }
    return ans;
}

double EvaluatePostfix(string exp, int vals[])
{
    Stack<double> s;
    double operand1, operand2;
    double cal;
    for (int i = 0; i < exp.length(); i++)
    {
        if (exp[i] == '+' || exp[i] == '-' || exp[i] == '*' || exp[i] == '/' || exp[i] == '^')
        {
            if (!s.isEmpty())
            {
                operand2 = s.getTop();
                s.pop();
                operand1 = s.getTop();
                s.pop();
                switch (exp[i])
                {
                case '+':
                    cal = operand1 + operand2;
                    break;
                case '-':
                    cal = operand1 - operand2;
                    break;
                case '*':
                    cal = operand1 * operand2;
                    break;
                case '/':
                    cal = operand1 / operand2;
                    break;
                case '^':
                    cal = pow(operand1, operand2);
                    break;
                default:
                    break;
                }
                s.push(cal);
            }
            else
            {
                cout << "Invalid Postfix expression given" << endl;
                return -1;
            }
        }
        else
        {
            s.push(vals[(int)exp[i] - 65]);
        }
    }
    if (!s.isEmpty())
    {
        return s.getTop();
    }
    else
    {
        cout << "Invalid Postfin expression" << endl;
        return -1;
    }
}

bool CheckParenthesis(string exp)
{
    Stack<char> s;
    for (int i = 0; i < exp.length(); i++)
    {
        if (exp[i] == '(')
        {
            s.push('(');
        }
        else if (exp[i] == ')')
        {
            s.pop();
        }
    }
    return s.isEmpty();
}

int main(void)
{
    cout << "Menu - Choose Option" << endl;
    cout << "1) Infix to Postfix" << endl;
    cout << "2) Infix to Prefix" << endl;
    cout << "3) Evalute Postfix" << endl;
    cout << "4) Check well formed parenthesis(PRACTICE PROBLEM)" << endl;
    int option;
    bool breakFlag = false;

    while (!breakFlag)
    {
        cout << "Menu Option: ";
        cin >> option;
        string s;
        switch (option)
        {
        case 1:
        {
            cout << "Input Experssion: ";
            cin >> s;
            cout << InfixToPostfix(s) << endl;
            break;
        }
        case 2:
        {
            cout << "Input Experssion: ";
            cin >> s;
            cout << InfixToPrefix(s) << endl;
            break;
        }
        case 3:
        {
            int variable_val;
            int vals[10];
            int no_of_variables;
            cout << "How Many variables: ";
            cin >> no_of_variables;
            for (int i = 0; i < no_of_variables; i++)
            {
                cout << "Value of " << (char)(i + 65) << ": ";
                cin >> variable_val;
                vals[i] = variable_val;
            }
            cout << "Input Experssion with variables ";
            for (int i = 0; i < no_of_variables; i++)
            {
                cout << (char)(i + 65);
                if (i != no_of_variables - 1)
                    cout << ", ";
            }
            cout << " : ";
            cin >> s;
            cout << to_string(EvaluatePostfix(s, vals)) << endl;
            break;
        }
        case 4:
        {
            cout << "Input Experssion: ";
            cin >> s;
            bool ans = CheckParenthesis(s);
            if (ans)
            {
                cout << "The Expression is well formed" << endl;
            }
            else
            {
                cout << "The Expression is not well formed" << endl;
            }
            break;
        }
        case -1:
        {
            breakFlag = true;
            break;
        }
        default:
            break;
        }
    }
    return 0;
}

/*
Output

---------------
Test Case 1
Evaluate the postfix expression AB*C+ , where A=4, B=5, C=6
---------------
Menu - Choose Option
1) Infix to Postfix
2) Infix to Prefix
3) Evalute Postfix
4) Check well formed parenthesis(PRACTICE PROBLEM)
Menu Option: 3
How Many variables: 3
Value of A: 4
Value of B: 5
Value of C: 6
Input Experssion with variables A, B, C : AB*C+
26.000000    
Menu Option: -1

---------------
Test Case 2
Evaluate the postfix expression ABC^^ , where A=2, B=3, C=4
---------------
Menu - Choose Option
1) Infix to Postfix
2) Infix to Prefix
3) Evalute Postfix
4) Check well formed parenthesis(PRACTICE PROBLEM)
Menu Option: 3
How Many variables: 3
Value of A: 2
Value of B: 3
Value of C: 4
Input Experssion with variables A, B, C : ABC^^
2417851639229258349412352.000000
Menu Option: -1

---------------
Test Case 3
Convert infix expression A*B+C into polish notation
---------------
Menu - Choose Option
1) Infix to Postfix
2) Infix to Prefix
3) Evalute Postfix
4) Check well formed parenthesis(PRACTICE PROBLEM)
Menu Option: 2
Input Experssion: A*B+C
+*ABC        
Menu Option: -1


---------------
Test Case 4
Convert infix expression A^B*C-C+D/A/(E+F) into polish notation
---------------
Menu - Choose Option
1) Infix to Postfix
2) Infix to Prefix
3) Evalute Postfix
4) Check well formed parenthesis(PRACTICE PROBLEM)
Menu Option: 2
Input Experssion: A^B*C-C+D/A/(E+F)
+-*^ABCC//DA+EF
Menu Option: -1

---------------
Test Case 5
Check well formed parenthesis
---------------
Menu - Choose Option
1) Infix to Postfix
2) Infix to Prefix
3) Evalute Postfix
4) Check well formed parenthesis(PRACTICE PROBLEM)
Menu Option: 4
Input Experssion: ((a*b)+c)
The Expression is well formed
Menu Option: 4
Input Experssion: ((a-b)+d
The Expression is not well formed
Menu Option: -1
*/