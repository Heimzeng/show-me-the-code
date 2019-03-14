#include <iostream>
#include <forward_list>
#include "printElements.cpp"
using namespace std;
int main(int argc, char const *argv[])
{
	forward_list<long> coll = {2, 3, 5, 7, 11, 13, 17};
	coll.resize(9);
	coll.resize(10, 99);
	printElements(coll, false);
	return 0;
}