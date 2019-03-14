#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

int main(){
	ifstream fin;
	fin.open("A-small-attempt10.in");
	ofstream fout;
	fout.open("out.txt");
	int T, A, N, P;
	fin >> T;
	for (int i = 0;i < T;i++){
		int remainder = 1;
		fin >> A >> N >> P;
		A = A % P;
		for (int k = 1;k<=N;k++){
			if (k!=1) A = remainder % P;
			for (int j = 0;j<k;j++)
   				remainder = (remainder * A) % P;
		}
		fout << "Case #" << i+1 << ": " << remainder << endl;
	}
	return 0;
}
