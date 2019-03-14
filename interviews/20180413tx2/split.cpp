#include <iostream>
using namespace std;

char** split(char* src, char* sep){
	if (src == NULL)
		return NULL;
	int num = 0;
	for (int i = 0;;i++){
		if(src[i] == '\0'){
			break;
		}
		for (int j=0;;j++){
			if(sep[j] == '\0')
				break;
			if(sep[j] == src[i]){
				num ++ ;
			}
		}
	}
	char** res = new char*[num + 1];
	int left = 0;
	int right = 0;
	int res_index = 0;
	bool getOne = false;
	bool isDone = false;
	for (int i = 0;;i++){
		if(src[i] == '\0'){
			right = i - 1;
			getOne = true;
			isDone = true;
		}
		for (int j=0;;j++){
			if(sep[j] == '\0')
				break;
			if(sep[j] == src[i]){
				getOne = true;
				right = i - 1;
			}
		}
		if(getOne){
			char* temp = new char(right - left + 2);
			int k = 0;
			for (; k + left <= right ; k++){
				temp[k] = src[k+left];
			}
			temp[k] = '\0';
			res[res_index] = temp;
			res_index += 1;
			getOne = false;
			left = right + 2;
		}
		if (isDone)
			break;
	}
	res[res_index] = NULL;
	return res;
}

int main(){
	char* src = "abc,def.efg;lll 000";
	char* sep = ",.; ";
	char** result = split(src, sep);
	int i = 0;
	while(result[i] != NULL){
		cout << result[i] << endl;
		i ++ ;
	}
	return 0;
}