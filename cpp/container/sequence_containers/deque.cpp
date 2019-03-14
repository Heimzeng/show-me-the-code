#include <iostream>
#include <deque>
#include "printElements.cpp"
using namespace std;
int main(int argc, char const *argv[])
{
	deque<float> coll;
	for (auto i=0;i<6;i++)
		coll.push_front(i*1.1);
	printElements(coll, false);
	return 0;
}