#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(int argc, char const *argv[])
{
	std::vector<int> v;
	for (auto i=0;i<5;i++)
		v.push_back(rand()%100);
	for (auto it=v.begin();it!=v.end();it++)
		cout << *it << " ";
	cout << endl;
	make_heap(v.begin(), v.end());
	for (auto it=v.begin();it!=v.end();it++)
		cout << *it << " ";
	cout << endl;
	pop_heap(v.begin(), v.end());
	v.pop_back();
	for (auto it=v.begin();it!=v.end();it++)
		cout << *it << " ";
	cout << endl;
	v.push_back(1928);
	push_heap(v.begin(), v.end());
	for (auto it=v.begin();it!=v.end();it++)
		cout << *it << " ";
	cout << endl;
	sort_heap(v.begin(), v.end());
	for (auto it=v.begin();it!=v.end();it++)
		cout << *it << " ";
	cout << endl;
	return 0;
}