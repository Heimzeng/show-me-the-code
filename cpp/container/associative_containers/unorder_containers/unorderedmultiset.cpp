#include <iostream>
#include <unordered_set>
#include <string>
using namespace std;

int main(int argc, char const *argv[])
{
	unordered_multiset<string> cities {
		"Braunschweig", "Hanover", "Frankfurt", "New York",
		"Chicago", "Toronto", "Paris", "Frankfurt"
	};
	for (const auto& elem : cities)
		cout << elem << ' ';
	cout << endl;
	cities.insert({"London", "Munich", "Hanover", "Braunschweig"});
	for (const auto& elem : cities)
		cout << elem << ' ';
	cout << endl;
	return 0;
}