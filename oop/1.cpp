//  Shreyas Balasaheb Gangurde SE A 25
// Implement a class Complex which represents the Complex Number data type.
// Implement the following 
// 	1. Constructor (including a default constructor which creates the complex number 0+0i). 
// 	2. Overloaded operator+ to add two complex numbers. 
// 	3. Overloaded operator* to multiply two complex numbers.
// 	4. Overloaded << and >> to print and read Complex Numbers.

#include<iostream>
using namespace std;

class Complex {
public: 
	int real, img;

// public:
// 1. Constructors
	Complex(int a, int b): real{a}, img{b} {};
	Complex(): real{0}, img{0} {};

// 2. + operator overloading
	Complex operator + (Complex const &obj) { 
		Complex res; 
		res.real = real + obj.real; 
		res.img = img + obj.img; 
		return res; 
	}

// 3. * operator overloading
	Complex operator * (Complex const &obj) { 
		Complex res; 
		res.real = ((real * obj.real) - (img * obj.img)); 
		res.img = ((real * obj.img) + (img * obj.real)); 
		return res; 
	}

// 4. Overloaded << and >>
	friend ostream &operator<<(ostream &outStream, const Complex &c)
    {
        outStream << c.real;
        if (c.img > 0)
            outStream << " + " << c.img << "i" << endl;
        else
            outStream << " - " << c.img * -1<< "i" << endl;
        return outStream;
    }

    friend istream &operator>>(istream &inStream, Complex &c)
    {
        cout << "Real Part: ";
        inStream >> c.real;
        cout << "Imaginary Part: ";
        inStream >> c.img;
        return inStream;
    }
};

int main() {
	Complex n1;
    Complex n2;
    cin >> n1;
    cin >> n2;
    Complex multiplication = n1 * n2;
    Complex addition = n1 + n2;
    cout << multiplication;
    cout << addition;
    
    return 0;
}