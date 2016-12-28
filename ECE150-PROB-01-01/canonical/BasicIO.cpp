#include <iostream>

using namespace std;

int main() {
	//DECLARING VARIABLES
	char name[21], address[21], city[21], province[21], country[21];
	long DOB, num;
	
	//INPUTTING DATA
	cout << endl <<"First Name: ";
	cin >> name;
	cout << "Date of birth (mmddyy): ";
	cin >> DOB;
	cout << "Student number: ";
	cin >> num;
	cout << "Email address: ";
	cin >> address;
	cout << "City: ";
	cin >> city;
	cout << "Province/state: ";
	cin >> province;
	cout << "Country: ";
	cin >> country;
	cout << "Thank you! sign-up is complete!" << endl;
	
	//PRINTING DATA
	cout << endl << "This is your sign-up receipt: ";
	cout << endl << "FIRST NAME: " << name;
	cout << endl << "DATE OF BIRTH (MMDDYY): " << DOB;
	cout << endl << "STUDENT NUMBER: " << num;
	cout << endl << "EMAIL ADDRESS: " << address;
	cout << endl << "CITY: " << city;
	cout << endl << "PROVINCE/STATE: " << province;
	cout << endl << "COUNTRY: " << country << endl << endl;
	
	return 0;
}
