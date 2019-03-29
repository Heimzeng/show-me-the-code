#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;
int main(int argc, char const *argv[])
{
	unordered_map<string, double> coll {{"tim", 9.9},
										{"heim", 11.1}, 
										};
	for (pair<const string, double>& elem : coll)
		elem.second *= elem.second;
	for (const auto& elem : coll)
		cout << elem.first << ": " << elem.second << endl;
	
	unordered_map<char, int> m;
	m['c'] = 0;
	m['b'] = 1;
	for (const auto& elem : m)
		cout << elem.first << ": " << elem.second << endl;
	auto i = m.find('c');
	if (m['c']==0)
		cout << "==" << endl;
	m.erase(i);
	for (const auto& elem : m)
		cout << elem.first << ": " << elem.second << endl;
	return 0;
}