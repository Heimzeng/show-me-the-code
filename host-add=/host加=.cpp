#include <iostream>
#include <fstream>
using namespace std;
int main(){
	ifstream fin;
	ofstream fout; 
	fin.open("hosts");
	fout.open("hostsss");
	string a,b;
	int i=0;
	for(i=0;i<3533;i++){
		fin>>a;
		fin>>b;
		fout<<a;
		fout<<'='<<b;
		fout<<endl;
	}
}
