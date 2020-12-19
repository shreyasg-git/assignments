// Write a C++ program create a calculator for an arithmetic operator (+, -, *, /). 
// The program should take two operands from user and performs the operation on those 
// two operands depending upon the operator entered by user. Use a switch statement to select the operation. 
// Finally, display the result.

// menu - 
// 0. Exit
// 1. Addition
// 2. Substraction
// 3. Multiplication
// 4. Division
#include<iostream>
using namespace std;

int main() {

	float a;
	float b;
	int choice;
	while (true) {

		float a;
		float b;
		int choice;
		cout << "Enter the first number :";
		cin >> a;
		cout << "\nEnter the second number :";
		cin >> b;

		cout << "\nChoose one option \n0. Exit\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division" << endl;
		cout << "Enter your choice : ";
		cin >> choice;
		switch(choice) {
			case 0:
				cout << "Exiting..." << endl;
				return 0;
				break;
			case 1:
				cout << "The Addition is " << a+b << endl;
				break;
			case 2:
				cout << "The Substraction is " << a - b << endl;
				break;
			case 3:
				cout << "The Multiplication is " << a * b << endl;
				break;
			case 4:
				cout << "The Division is " << a / b << endl;
				break;
		}
	}
	


	return 0;
}