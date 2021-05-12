/*


Pizza parlor accepting maximum M orders. 
Orders are served in first come first served basis. 
Order once placed cannot be cancelled. 
Write C++ program to simulate the system using 
circular queue using array
*/

#include <iostream>
#include <string>
using namespace std;
#define size 10

template <typename T>
class ACQueue
{
    T q[size];
    int front, rear;

public:
    ACQueue()
    {
        front = -1;
        rear = 0;
    }

    void init()
    {
        for (int i = 0; i < size; i++)
        {
            q[i] = 0;
        }
    }

    void Insert(int new_val)
    {
        if (front == (rear + 1) % size)
        {
            cout << "Queue is full" << endl;
        }
        else
        {
            if (front == -1)
                front = rear = 0;
            else
                rear = (rear + 1) % size;
            q[rear] = new_val;
        }
    }

    void Delete()
    {
        if (front == -1)
        {
            cout << "Queue is empty" << endl;
            return;
        }
        T val = q[front];
        if (front == rear)
        {
            front = rear = -1;
        }
        else
        {
            front = (front + 1) % size;
        }
    }

    T GetFront()
    {
        if (front == -1)
        {
            cout << "Queue is Empty" << endl;
            return 0;
        }
        else
        {
            return q[front];
        }
    }
};

template <typename T>
class LCQueue
{

    struct Node
    {
        T value;
        Node *next;
    };
    Node *head;
    Node *tail;

public:
    LCQueue()
    {
        head = new Node;
        Node *current = head;
        for (int i = 0; i < size; i++)
        {
            current->value = 0;
            current->next = new Node;
            current = current->next;
        }
        current->next = head;
        tail = head;
    }

    void Insert(int new_val)
    {
        if (tail->next == head)
        {
            cout << "Queue is Full" << endl;
        }
        else
        {
            tail->value = new_val;
            tail = tail->next;
        }
    }

    T GetFront()
    {
        if (head == tail)
        {
            cout << "Queue is empty" << endl;
            return 0;
        }
        else
        {
            return head->value;
        }
    }

    void Delete()
    {
        if (head == tail)
        {
            cout << "Queue is empty" << endl;
            return;
        }
        else
        {
            head = head->next;
        }
    }
};

int main(void)
{
    cout << "Menu - Circular Queue Type" << endl;
    cout << "1) Array Circular queue" << endl;
    cout << "2) Linked List Circular Queue (PRACTICE PROBLEM)" << endl;
    while (true)
    {
        int option;
        cout << "Menu Option: ";
        cin >> option;

        if (option == 1)
        {
            ACQueue<int> pizzaParlor;
            // Inserting initial 5 elements
            pizzaParlor.Insert(1);
            pizzaParlor.Insert(2);
            pizzaParlor.Insert(3);
            pizzaParlor.Insert(4);
            pizzaParlor.Insert(5);
            // Test Case
            pizzaParlor.Delete();
            pizzaParlor.Insert(10);
            pizzaParlor.Insert(20);
            pizzaParlor.Delete();
            cout << to_string(pizzaParlor.GetFront()) << endl;
            pizzaParlor.Insert(30);
            pizzaParlor.Insert(40);
            pizzaParlor.Insert(50);
            pizzaParlor.Insert(60);
            pizzaParlor.Delete();
            pizzaParlor.Delete();
            pizzaParlor.Delete();
            cout << to_string(pizzaParlor.GetFront()) << endl;
            pizzaParlor.Insert(70);
        }
        else if (option == 2)
        {
            LCQueue<int> pizzaParlor;
            // Inserting initial 5 elements
            pizzaParlor.Insert(1);
            pizzaParlor.Insert(2);
            pizzaParlor.Insert(3);
            pizzaParlor.Insert(4);
            pizzaParlor.Insert(5);
            // Test Case
            pizzaParlor.Delete();
            pizzaParlor.Insert(10);
            pizzaParlor.Insert(20);
            pizzaParlor.Delete();
            cout << to_string(pizzaParlor.GetFront()) << endl;
            pizzaParlor.Insert(30);
            pizzaParlor.Insert(40);
            pizzaParlor.Insert(50);
            pizzaParlor.Insert(60);
            pizzaParlor.Delete();
            pizzaParlor.Delete();
            pizzaParlor.Delete();
            cout << to_string(pizzaParlor.GetFront()) << endl;
            pizzaParlor.Insert(70);
        }
        else if (option == -1)
            break;
        else
            cout << "Invalid Input" << endl;
    }
    return 0;
}

/*
Output

----------------
Test Case 1

Consider the linear queue of size 5 and perform 
following operations in sequence
1.	Delete()
2.	Insert (10)
3.	Insert(20)
4.	Delete()
5.	Getfront()
6.	Insert (30)
7.	Insert (40)
8.	Insert (50)
9.	Insert(60)
10.	Delete()
11.	Delete()
12.	Delete()
13.	Getfront()
14.	Insert(70)
----------------

Menu - Circular Queue Type
1) Array Circular queue
2) Linked List Circular Queue (PRACTICE PROBLEM)
Menu Option: 1 // Doing test case with array based circular queue
3
10
Menu Option: 2 // Doing same test case with linked list based circular queue
3
10
Menu Option: -1 
*/