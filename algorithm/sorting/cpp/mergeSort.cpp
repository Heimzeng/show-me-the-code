#include <iostream>
#include <vector>

void merge(vector<int>& list, int l, int m, int r){
	int i, j, k;
	int n1 = m - l + 1;
	int n2 = r - m;
	int L[n1], R[n2];
	for (i = 0; i<n1; i++)
		L[i] = list[l+i];
	for (j = 0;j<n2;j++)
		R[j] = list[m+1+j];
	i = 0;
	j = 0;
	k = l;
	while(i < n1 && j < n2)
	{
		if(L[i] < R[j]){
			list[k] = L[i];
			i ++;
		}
		else{
			list[k] = R[j];
			j ++;
		}
		k ++;
	}
	while(i<n1){
		list[k] = L[i];
		i ++;
		k ++;
	}
	while(j<n2){
		list[k] = R[j];
		k ++;
		j ++;
	}
}

void mergeSort(vector<int>& list, int l, int r){
	if (l < r){
		int m = l + (r - l) / 2;
		mergeSort(list, l, m);
		mergeSort(list, m + 1, r);
		merge(list, l, m, r);
	}
}

void bubbleSort(vector<int>& list){
	for (auto i=list.begin();i!=list.end();i++){
		for (auto j=i+1;j!=list.end();j++){
			if (*j < *i){
				int temp = *i;
				*i = *j;
				*j = temp;
			}
		}
	}
}

void exchangeSort(vector<int>& list){
	for (auto i=list.begin();i!=list.end();i++){
		auto maxi = i;
		for (auto j=i+1;j!=list.end();j++){
			if (*j < *maxi)
				maxi = j;
		}
		if (maxi != i){
			int temp = *i;
			*i = *maxi;
			*maxi = temp;
		}
	}
}

void insertSort(vector<int>& list){
	//don't want to code it
}