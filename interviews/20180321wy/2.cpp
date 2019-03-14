#include <iostream>
#include <string>
using namespace std;

int getSum(string str){
	int sum = 0;
	int len = str.size();
	if (len == 1){
		return 1;
	}
	else{
		
	}
}

int getTheCode(string str){
	int len = str.size();
	int res = 0;
	char first = str[0];
	while(first != 'a'){
		str[0] = str[0] - 1;
		res += getSum(str);
	}
	//res += getTheCode(str.substr(1,len-1));
	return res;
}

int main(){
	int N;
	cin >> N;
	for (int i = 0;i < N; i++){
		string in;
		cin >> in;
		getTheCode(in);
	}
	return 0;
}