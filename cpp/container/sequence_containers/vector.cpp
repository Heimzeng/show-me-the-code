#include <iostream>
#include <vector>
#include "printElements.cpp"
using namespace std;

int main(int argc, char const *argv[])
{
	vector<int> coll;
	for (auto i=1;i<=6;i++)
		coll.push_back(i);
	printElements(coll, false);
	return 0;
}