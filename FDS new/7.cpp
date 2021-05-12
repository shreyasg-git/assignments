/*

Department of Computer Engineering has student's club named 'Pinnacle Club'.
Students of second, third and final year of department can be
granted membership on request. Similarly one may cancel the membership of club.
First node is reserved for president of club and last node is reserved for
secretary of club. Write C++ program to maintain club member‘s information
using singly linked list. Store student PRN and Name. Write functions to:
a)	Add and delete the members as well as president or even secretary.
b)	Compute total number of members of club
c)	Display members
D)  Two linked lists exists for two divisions. Concatenate two lists.
*/
#include <iostream>
#include <string>
using namespace std;
struct Node
{
    int PRN;
    string Name;
    Node *next;
};
class LinkedList
{
    Node *head;
    int length = 0;

public:
    LinkedList();
    void deleteMember(int index);
    void addMember(int index, int prn, string name);
    void display();
    void concat(LinkedList &newlist);
    int totalMembers();
};

LinkedList::LinkedList()
{
    head = NULL;
}

void LinkedList::deleteMember(int index)
{
    int counter = 0;
    Node *current = head;
    Node *previous = NULL;
    while (true)
    {

        if (index == counter)
        {
            if (previous == NULL)
            {
                head = current->next;
            }
            else
            {
                previous->next = current->next;
            }
            length--;
            break;
        }
        if (current == NULL)
        {
            cout << "The given index does not exist" << endl;
            break;
        }
        previous = current;
        current = current->next;
        counter++;
    }
}

void LinkedList::addMember(int index, int prn, string name)
{
    Node *current = head;
    Node *previous = NULL;
    int counter = 0;
    while (true)
    {
        if (index == counter)
        {
            if (previous == NULL)
            {
                Node *temp = head;
                head = new Node;
                head->Name = name;
                head->PRN = prn;
                head->next = temp;
            }
            else
            {
                previous->next = new Node;
                previous->next->Name = name;
                previous->next->PRN = prn;
                previous->next->next = current;
            }
            length++;
            break;
        }
        if (current == NULL)
        {
            cout << "The given index does not exist" << endl;
            break;
        }
        previous = current;
        current = current->next;
        counter++;
    }
}

void LinkedList::display()
{
    Node *current = head;
    cout << "[ ";
    while (true)
    {
        if (current == NULL)
            break;
        cout << "( " << current->PRN << ", " << current->Name << " )";
        current = current->next;
        if (current != NULL)
            cout << ", ";
    }
    cout << " ]" << endl;
}

void LinkedList::concat(LinkedList &newlist)
{
    Node *current = head;
    while (true)
    {
        if (current->next == NULL)
        {
            current->next = newlist.head;
            break;
        }
        current = current->next;
    }
}

int LinkedList::totalMembers()
{
    return length;
}

int main(void)
{
    LinkedList Members1;
    Members1.addMember(0, 111111, "Atharva");
    Members1.addMember(1, 111112, "Rahul");
    Members1.display();
    cout << "Total Number of members in list 1 :- " << Members1.totalMembers() << endl;
    LinkedList Members2;
    Members2.addMember(0, 111113, "Manas");
    Members2.addMember(1, 111114, "Mehul");
    Members2.display();
    cout << "Total Number of members in list 2 :- " << Members2.totalMembers() << endl;
    Members1.deleteMember(1);
    Members1.display();
    Members1.concat(Members2);
    Members1.display();

    return 0;
}

/*
Output 

[ ( 111111, Atharva ), ( 111112, Rahul ) ]  // addMember operation output for Linked List 1
Total Number of members in list 1 :- 2
[ ( 111113, Manas ), ( 111114, Mehul ) ]    // addMember operation output Linked List 2
Total Number of members in list 2 :- 2
[ ( 111111, Atharva ) ]                     // deleteMember operation output for Linked List 1
[ ( 111111, Atharva ), ( 111113, Manas ), ( 111114, Mehul ) ]   // concat operation output
*/