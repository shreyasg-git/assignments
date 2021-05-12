/*

Queues are frequently used in computer programming, 
and a typical example is the creation of a job queue by an 
operating system. If the operating system does not use priorities, 
then the jobs are processed in the order they enter the system. 
Write C++ program for simulating job queue. 
Write functions to add job and delete job from queue.
*/

#include <iostream>
#include <string>
using namespace std;
#define size 30

template <typename T>
class AQueue
{
    int head_index;
    int insert_index;
    int length;
    T q[size];

public:
    AQueue()
    {
        head_index = 0;
        insert_index = 0;
        length = 0;
    }
    void Insert(T new_val)
    {
        q[insert_index] = new_val;
        insert_index++;
        length++;
    }

    T GetFront()
    {
        int val = q[head_index];
        return val;
    }

    void Delete()
    {
        if (length > 0)
        {
            head_index++;
            length--;
        }
    }

    bool isEmpty()
    {
        return length == 0;
    }
};

template <typename T>
class LLQueue
{
    struct Node
    {
        T value;
        Node *next;
    };
    Node *head;
    Node *tail;
    int length;

public:
    LLQueue()
    {
        head = NULL;
        tail = NULL;
        length = 0;
    }
    void Insert(T new_val)
    {
        Node *new_tail = new Node;
        new_tail->value = new_val;
        new_tail->next = NULL;
        if (head == NULL && tail == NULL)
        {
            head = new_tail;
            tail = head;
        }
        else
        {
            tail->next = new_tail;
            tail = new_tail;
        }
        length++;
    }

    T GetFront()
    {
        return head->value;
    }

    void Delete()
    {
        head = head->next;
        length--;
    }

    bool isEmpty()
    {
        return length == 0;
    }
};

int main(void)
{
    cout << "Menu - Queue Type" << endl;
    cout << "1) Array queue" << endl;
    cout << "2) Linked List Queue (PRACTICE PROBLEM)" << endl;
    while (true)
    {
        int option;
        cout << "Menu Option: ";
        cin >> option;

        if (option == 1)
        {
            AQueue<int> jobQueue;
            // Inserting initial 5 elements
            jobQueue.Insert(1);
            jobQueue.Insert(2);
            jobQueue.Insert(3);
            jobQueue.Insert(4);
            jobQueue.Insert(5);
            // Test Case
            jobQueue.Delete();
            jobQueue.Insert(10);
            jobQueue.Insert(20);
            jobQueue.Delete();
            cout << to_string(jobQueue.GetFront()) << endl;
            jobQueue.Insert(30);
            jobQueue.Insert(40);
            jobQueue.Insert(50);
            jobQueue.Insert(60);
            jobQueue.Delete();
            jobQueue.Delete();
            jobQueue.Delete();
            cout << to_string(jobQueue.GetFront()) << endl;
            jobQueue.Insert(70);
        }
        else if (option == 2)
        {
            LLQueue<int> jobQueue;
            // Inserting initial 5 elements
            jobQueue.Insert(1);
            jobQueue.Insert(2);
            jobQueue.Insert(3);
            jobQueue.Insert(4);
            jobQueue.Insert(5);
            // Test Case
            jobQueue.Delete();
            jobQueue.Insert(10);
            jobQueue.Insert(20);
            jobQueue.Delete();
            cout << to_string(jobQueue.GetFront()) << endl;
            jobQueue.Insert(30);
            jobQueue.Insert(40);
            jobQueue.Insert(50);
            jobQueue.Insert(60);
            jobQueue.Delete();
            jobQueue.Delete();
            jobQueue.Delete();
            cout << to_string(jobQueue.GetFront()) << endl;
            jobQueue.Insert(70);
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

Menu - Queue Type
1) Array queue
2) Linked List Queue (PRACTICE PROBLEM)
Menu Option: 1 // Doing test case with array based queue
3
10
Menu Option: 2 // Doing same test case with linked list based queue
3
10
Menu Option: -1 
*/