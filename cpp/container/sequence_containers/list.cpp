#include <iostream>
#include <list>
#include "printElements.cpp"
using namespace std;

int main(int argc, char const *argv[])
{
	list<char> coll;
	for (auto c='a';c<='z';c++)
		coll.push_back(c);
	for (auto elem : coll){
		elem += 1;  //do nothing with the coll list
	}
	//if you want to modify elements
	for (auto& elem : coll)
		elem += 1;
	for (auto it=coll.begin();it!=coll.end();it++)
		*it += 1;	
	//end if
	printElements(coll, false);
	return 0;
}