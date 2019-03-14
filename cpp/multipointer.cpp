#include <iostream>
#include <vector>
using namespace std;
int main(int argc, char const *argv[])
{
	int* intlistptr = new int[10] {1, 2, 3, 4, 5};
	for (auto i=intlistptr;i<intlistptr+10;i++)
		cout << *i << " ";
	cout << endl;
	int row_num = 10;
	int col_num = 10;
	char string_list[row_num][col_num];
	//char** string_list_ptr = new char[row_num][col_num];
	char* str1 = new char[10] {'a', 'p', 'p', 'l', 'e'};
	for (auto i=str1;i<str1+10;i++)
		cout << *i ;
	cout << endl;
	char* str2 = "abc,def.efg;lll 000";
	char** sl = new char* [10];
	*sl = str2;
	*(sl+1) = str1;
	*(sl+2) = nullptr;
	for (auto sit = sl;sit != nullptr;sit ++){
		for (auto it = sit;it < sit + 10;it++){
			cout << *it ;
		}
		cout << endl;
	}
	return 0;
}