/*

A double-ended queue (deque) is a linear list in which 
additions and deletions may be made at either end. 
Obtain a data representation mapping a deque 
into a one- dimensional array. Write C++ program 
to simulate deque with functions to add and delete 
elements from either end of the deque.

*/
#include <iostream>
#include <string>
using namespace std;
#define size 10

template <typename T>
class LDQueue
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
    LDQueue()
    {
        length = 0;
        head = NULL;
        tail = NULL;
    }

    void InsertFront(T new_val)
    {
        if (head == NULL && tail == NULL)
        {
            head = new Node;
            head->value = new_val;
            tail = head;
        }
        else
        {
            Node *temp = new Node;
            temp->value = new_val;
            temp->next = head;
            head = temp;
        }
    }

    void InsertLast(T new_val)
    {
        if (head == NULL && tail == NULL)
        {
            head = new Node;
            head->value = new_val;
            tail = head;
        }
        else
        {
            tail->next = new Node;
            tail = tail->next;
            tail->value = new_val;
        }
    }

    int GetFront()
    {
        if (head != NULL)
            return head->value;
        cout << "Linked List is Empty" << endl;
        return 0;
    }

    int GetLast()
    {
        if (tail != NULL)
            return tail->value;
        cout << "Linked List is empty" << endl;
        return 0;
    }

    void DeleteFront()
    {
        if (head != NULL)
        {
            head = head->next;
        }
    }

    void DeleteLast()
    {
        Node *current = head;
        while (current != NULL)
        {
            if (current->next == tail)
            {
                tail = current;
                return;
            }
            current = current->next;
        }
    }
};

template <typename T>
class ADQueue
{
    T q[size];

public:
    int front, rear;
    ADQueue()
    {
        front = -1;
        rear = -1;
        for (int i = 0; i < size; i++)
        {
            q[i] = -1;
        }
    }

    void InsertFront(T new_val)
    {
        if (front == -1)
            front++;
        int i = front - 1;
        while (i >= 0)
        {
            q[i + 1] = q[i];
            i--;
        }
        int j = rear;
        while (j >= front)
        {
            q[j + 1] = q[j];
            j--;
        }
        rear++;
        q[front] = new_val;
    }

    void InsertLast(T new_val)
    {
        if (front == -1 && rear == -1)
            front++;
        q[++rear] = new_val;
    }

    void DeleteFront()
    {
        T item;
        if (front == -1)
            front++;
        item = q[front];
        q[front] = -1;
        front++;
    }

    void DeleteLast()
    {
        T item;
        item = q[rear];
        q[rear] = -1;
        rear--;
    }

    T GetFront()
    {
        return q[front];
    }

    T GetLast()
    {
        return q[rear];
    }
};

int main()
{

    cout << "Menu - DQueue Type" << endl;
    cout << "1) Array Dqueue" << endl;
    cout << "2) Linked List DQueue (PRACTICE PROBLEM)" << endl;
    while (true)
    {
        int option;
        cout << "Menu Option: ";
        cin >> option;

        if (option == 1)
        {
            ADQueue<int> q;
            q.InsertLast(5);
            q.InsertLast(6);
            cout << to_string(q.GetLast()) << endl;
            cout << to_string(q.GetFront()) << endl;
            q.InsertFront(4);
            q.InsertLast(7);
            cout << to_string(q.GetLast()) << endl;
            cout << to_string(q.GetFront()) << endl;
            q.DeleteFront();
            q.DeleteLast();
            cout << to_string(q.GetLast()) << endl;
            cout << to_string(q.GetFront()) << endl;
        }
        else if (option == 2)
        {
            LDQueue<int> q;
            q.InsertLast(5);
            q.InsertLast(6);
            cout << to_string(q.GetLast()) << endl;
            cout << to_string(q.GetFront()) << endl;
            q.InsertFront(4);
            q.InsertLast(7);
            cout << to_string(q.GetLast()) << endl;
            cout << to_string(q.GetFront()) << endl;
            q.DeleteFront();
            q.DeleteLast();
            cout << to_string(q.GetLast()) << endl;
            cout << to_string(q.GetFront()) << endl;
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

Menu - DQueue Type
1) Array Dqueue
2) Linked List DQueue (PRACTICE PROBLEM)
Menu Option: 1
6
5
7
4
6
5
Menu Option: 2
6
5
7
4
6
5
Menu Option: -1

*/