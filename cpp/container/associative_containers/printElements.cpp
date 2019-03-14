#include <iostream>
using namespace std;
template <typename T>
//use const to avoid a copy operation?
void printElements(const T& coll, bool isLineByLine){
	for (const auto& elem : coll){
		cout << elem ;
		if (isLineByLine)
			cout << endl;
		else
			cout << ' ';
	}
	if (!isLineByLine)
		cout << endl;
}