#include <iostream>
#include <array>
#include <string>
#include "printElements.cpp"
using namespace std;
int main(int argc, char const *argv[])
{
	array<string, 5> coll = {"hello", "world" };
	printElements(coll, true);
	return 0;
}