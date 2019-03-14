#include <iostream>
using namespace std;
int main(int argc, char const *argv[])
{
	int i = -1;
	uint j = i;
	cout << j << endl;
	i = j;
	cout << i << endl;
	cout << int(j) << endl;
	return 0;
}