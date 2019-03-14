#include <iostream>
#include <algorithm>

using namespace std;

void FullPermutation(int array[]){
	do
	{
		for (int i = 0; i < 4; i++)
			cout << array[i] << " ";
		cout << endl;
	}while (next_permutation(array, array + 4));
}

int main(){
	int array[4] = {1, 2, 3, 4 };

	FullPermutation(array);

	return 0;
}