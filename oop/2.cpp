// Shreyas Balasaheb Gangurde SE A 25
// Develop a program in C++ to create a database of student’s information system containing the
// following information: Name, Roll number, Class, Division, Date of Birth, Blood group, Contact
// address, Telephone number, Driving license no. and other. Construct the database with
// suitable member functions. Make use of constructor, default constructor, copy constructor,
// destructor, static member functions, friend class, this pointer, inline code and dynamic
// memory allocation operators-new and delete as well as exception handling.


#include<iostream>
#include<string>
#include<vector>

using namespace std;

class PersonMoreInfo {
private: 
	string blood, contAddress, tele, drivingLicense;
	friend class PersonBasicInfo;
public:
	PersonMoreInfo(): blood{"Default"}, contAddress{"Default"}, tele{"Default"}, drivingLicense{"Default"} {};
};


class PersonBasicInfo {
private:
	string name, cls, div, dob; 
	int roll;
	friend class PersonMoreInfo;

public:
	static int count;
	// default constructors (initialiser list syntax) - 
	PersonBasicInfo(): name{"Default"}, cls{"Default"}, div{"Default"}, dob{"01.01.0001"}, roll{0} {};
	// copy constructor
	void PersonAllInfoInput(PersonMoreInfo *moreInfo);
	void PersonAllInfoOutput(PersonMoreInfo *moreInfo);
	static void DisplayCount() {
		cout << "There are total " << count << " records in database" << endl;
	};

}; 

int PersonBasicInfo::count = 0;

void PersonBasicInfo::PersonAllInfoInput(PersonMoreInfo *moreInfo) {
	cout << "Roll No : ";
    cin >> this->roll;
    cout << "Name : ";
    cin >> this->name;
    cout << "Class : ";
    cin >> this->cls;
    cout << "Division : ";
    cin >> this->div;
    cout << "Date Of Birth : ";
    cin >> this->dob;
    cout << "Blood Group : ";
    cin >> moreInfo->blood;
    cout << "Address : ";
    cin >> moreInfo->contAddress;
    cout << "Telephone Number : ";
    cin >> moreInfo->tele;
    cout << "Driving License Number : ";
    cin >> moreInfo->drivingLicense;
   
    this->count++;
}

void PersonBasicInfo::PersonAllInfoOutput(PersonMoreInfo *moreInfo) {
	cout << "Roll No : ";
    cout << this->roll << endl;
    cout << "Name : ";
    cout << this->name << endl;
    cout << "Class : ";
    cout << this->cls << endl;
    cout << "Division : ";
    cout << this->div << endl;
    cout << "Date Of Birth : ";
    cout << this->dob << endl;
    cout << "Blood Group : ";
    cout << moreInfo->blood << endl;
    cout << "Address : ";
    cout << moreInfo->contAddress << endl;
    cout << "Telephone Number : ";
    cout << moreInfo->tele << endl;
    cout << "Driving License Number : ";
    cout << moreInfo->drivingLicense << endl;
};

int main() {

	vector <PersonBasicInfo*> basic;
	vector <PersonMoreInfo*> more;
    int index = 0, choice;
    char ans;
    do
    {
        cout << "Menu" << endl;
        cout << "1) Input Data\n"
             << "2) Display Data\n"
             << "Enter Your Choice";
        cin >> choice;
        switch (choice)
        {
        case 1:
            cout << "------Enter Detail------" << endl;
            do
            {
                basic.push_back(new PersonBasicInfo);
                more.push_back(new PersonMoreInfo);
                basic[index]->PersonAllInfoInput(more[index]);
                index++;
                PersonBasicInfo::DisplayCount();
                cout << "\nDo you want to add more records(y/n)? ";
                cin >> ans;
            } while (ans == 'y' || ans == 'Y');
            break;
        case 2:
            cout << "\n-------Displaying Data--------" << endl;
            for (int i = 0; i < index; i++)
            {
                cout << "\tRecord " << i + 1 << endl;
                basic[i]->PersonAllInfoOutput(more[i]);
            }
            break;
        default:
            break;
        }
        cout << "\nDo you want to go to main menu(y/n)? ";
        cin >> ans;
        cin.ignore(1, '\n');
    } while (ans == 'y' || ans == 'Y');
    return 0;

	return 0;
}