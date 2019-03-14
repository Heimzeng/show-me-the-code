#include <set>
#include <iostream>
#include <string>
#include "printElements.cpp"
using namespace std;
int main(int argc, char const *argv[])
{
	multiset<string> cities {
		"Guangzhou", "Shanghai", "Shenzhen", "Beijing", "New York", "Tokyo",
		"Zhuhai", "Hong Kong", "Macao", 
	};
	printElements(cities, false);
	cities.insert({"London", "Tianjin", "Taibei", "Guangzhou"});
	printElements(cities, false);
	return 0;
}