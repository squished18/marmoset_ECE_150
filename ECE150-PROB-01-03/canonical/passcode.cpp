#include <iostream>
using namespace std;
int main() {
	
	//declare variables for inputs
	//Eg. First name is Joe. Last name is Doe. 
	cout << "Enter three characters consecutively without space: ";

	unsigned char A;     
	unsigned char B; 
	unsigned char C; 
	
	//input the following: 
	cin >> A >> B >> C;
	
	//Convert last name to ASCII 
	unsigned int A_ASCII = A;
	unsigned int B_ASCII = B;
	unsigned int C_ASCII = C;
	unsigned int passcode = 1000000*A_ASCII + 1000*B_ASCII + C_ASCII;  
	
	//output this sentence, including ASCII conversion. 
	cout << "The corresponding passcode is: " << passcode << endl;
	
}