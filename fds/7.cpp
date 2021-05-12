#include<iostream>
#include<string>
using namespace std;

// A student class
// adding a node at given index
// removing node acc to student name
// 

struct Member {
	string PRN;
	string name;
	Member *next;
	Member(string PRN,string name): PRN{PRN}, name{name}, next{nullptr} {}
	Member(): PRN{NULL}, name{NULL}, next{nullptr} {
		cout << "empty Member initiated" << endl;
	} 
};

class MemberDataBase {
private:
	Member * head;
	int length = 0;
	Member * lastNode;

public:
	MemberDataBase(Member * member) {
		head = member;
		lastNode = member;
		length ++;
	}

	
	void addMember(Member * member, int index) {
		if(index > length) {
			cout << "Insertion Index Out Of Range" << endl;
			return;
		}
		// if(index == )
		// cout << member << endl;
		Member * currentNode = head;
		for(int i = 0;i<index - 1; i++) {
			cout << '(' << i << ')';

			cout << '{'; 
			cout << currentNode->name;
			cout << ", "; 
			cout << currentNode->PRN;
			cout << "} -> ";
			cout << currentNode->next;

			currentNode = currentNode-> next;
		}
		Member *temp = currentNode -> next; 
		currentNode -> next = member;
		member -> next = temp;

		length++;
		cout <<"member added successfully" << member -> PRN << endl;
		// cout << length << endl;

		return;
	}
	void print() {
		cout << "\nPrinting The Linked List" << endl;
		Member *crntNode = head;
		cout << length << endl;
		// cout << crntNode->name;
		// for(int i = 0; i<length ; i++) {
		// 	if(crntNode == nullptr) {
		// 		break;
		// 	}
		// 	cout << '{'; 
		// 	cout << crntNode->name;
		// 	cout << ", "; 
		// 	cout << crntNode->PRN;
		// 	cout << "} -> ";
		// 	cout << crntNode->next;

		// 	crntNode = crntNode -> next;

		// }
		while(crntNode != nullptr) {
				cout << '{'; 
				cout << crntNode->name;
				cout << ", "; 
				cout << crntNode->PRN;
				cout << "} -> ";
				cout << crntNode->next;

				crntNode = crntNode -> next;
		}
		cout << "\nPrinting Ended ----" << endl;
		return;
	}
};

int main() {
	Member *one = new Member("72020120", "Shreyas0");
	Member *two = new Member("72020121", "Shreyas1");
	Member *three = new Member("72020122", "Shreyas2");
	Member *four = new Member("72020123", "Shreyas3");
	Member *five = new Member("72020124", "Shreyas4");
	// Member *six = new Member("72020124", "Shreyas4");
	
	MemberDataBase divA = MemberDataBase(one); 
	divA.print();
	
	divA.addMember(two, 1);
	divA.print();

	divA.addMember(three, 2);
	divA.print();
	divA.addMember(four, 3);
	divA.print();
	divA.addMember(three, 4);
	divA.print();
	divA.addMember(five, 5);
	divA.print();

	return 0;
}