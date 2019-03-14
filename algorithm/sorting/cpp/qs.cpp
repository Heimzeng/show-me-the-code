#include <iostream>
#include <vector>
using namespace std;
void quickSort(vector<int>& list, vector<int>::iterator begin, vector<int>::iterator end){
	if (end <= begin)
		return ;
	auto p = begin;
	auto i = begin + 1;
	auto j = end;
	while(1){
		while(*i <= *p && i < end)
			i ++;
		while(*j >= *p && j > begin + 1)
			j --;
		if (i < j){
			*i += *j;
			*j = *i - *j;
			*i -= *j;
		}
		else{
			if (*j < *p){
				*p += *j;
				*j = *p - *j;
				*p -= *j;
			}
			break;
		}
	}
	quickSort(list, begin, j - 1);
	quickSort(list, j + 1, end);
}

bool checkSorted(vector<int>& list){
	for (auto it=list.begin();it!=list.end()-1;it++){//少了个-1啊啊啊
		if (*it > *(it+1))
			return false;
	}
	return true;
}

void quickSort(vector<int>& list, int begin, int end){
	if (end <= begin)
		return ;
	int p = list[begin];
	int i = begin + 1;
	int j = end;
	while(1){
		while(list[i] <= p && i < end)
			i ++;
		while(list[j] >= p && j > begin + 1)
			j --;
		if (i < j){
			int temp = list[i];
			list[i] = list[j];
			list[j] = temp;
		}
		else{
			if (list[j] < p){
				list[begin] = list[j];
				list[j] = p;
			}
			break;
		}
	}
	quickSort(list, begin, j - 1); // if change "j - 1" to "j" will cause segement fault
	quickSort(list, j + 1, end);
}
