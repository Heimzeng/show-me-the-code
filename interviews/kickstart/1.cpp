#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

int main(){
	ifstream fin;
	fin.open("A-small-attempt.in");
	ofstream fout;
	fout.open("out.txt");
	int T, A, N, P;
	fin >> T;
	for (int i = 0;i < T;i++){
		int remainder = 1;
		int index = 0;
		fin >> A >> N >> P;
		for (int j = 1;j <= N;j++){
			
			remainder = remainder * (int)pow(A,j) % P;
		}
		remainder = remainder % P;
		fout << "Case #" << i+1 << ": " << remainder << endl;
	}
	return 0;
}
