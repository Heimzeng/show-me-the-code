#include <iostream>
#include "qs.cpp"
#include "mergeSort.cpp"
#include <algorithm>

int main(int argc, char const *argv[])
{
	vector<int> v;
	for (auto i=0;i<5;i++)
		v.push_back(rand()%100);
	for (auto it=v.begin();it!=v.end();it++)
		cout << *it << " ";
	cout << endl;
	cout << checkSorted(v) << endl;
	//quickSort(v, 0, v.size()-1);
	//quickSort(v, v.begin(), v.end() - 1);
	//mergeSort(v, 0, v.size()-1);
	//bubbleSort(v);
	//exchangeSort(v);
	//stable_sort(v.begin(), v.end());
	sort(v.begin(), v.end(), greater<int>());
	for (auto it=v.begin();it!=v.end();it++)
		cout << *it << " ";
	cout << endl;
	cout << checkSorted(v) << endl;
	return 0;
}