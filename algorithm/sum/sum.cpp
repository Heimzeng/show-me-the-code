//不用'+', '-', '*', '/'实现两个整数相加
#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int numA, numB;
	cin >> numA >> numB;
	int sum, carry;
	while(true){
		sum = numA ^ numB;
		carry = (numA & numB) << 1;

		numA = sum;
		numB = carry;

		if (numB == 0)
			break;
	}
	cout << numA << endl;
	return 0;
}