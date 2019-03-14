#include <iostream>
#include <math.h>
using namespace std;

class Line{
public:
	bool isKInifite;
	float k;
};

int main(){
	int N;
	cin >> N;
	for(int i=0;i<N;i++){
		int x[4];
		int y[4];
		cin >> x[0] >> x[1] >> x[2] >> x[3];
		cin >> y[0] >> y[1] >> y[2] >> y[3];
		Line line[6];
		int indexL = 0;
		bool pass = true;
		for(int j=0;j<4;j++){
			for(int l=j+1;l<4;l++){
				if(x[j] == x[l]){
					line[indexL].isKInifite = true;
				}
				else{
					line[indexL].isKInifite = false;
					line[indexL].k = (float(y[j]) - float(y[l])) / (float(x[j]) - float(x[l]));
				}
			}
		}
		for(int j=0;j<6;j++){
			for(int l=j+1;l<6;l++){
				if(line[j].isKInifite){
					if(!line[l].isKInifite && line[l].k != 0){
						pass = false;
						break;
					}
				}
				else if(line[l].isKInifite){
					if(line[j].k != 0){
						pass = false;
						break;
					}
				}
				else{
					if(!(line[j].k-line[l].k == 0 | line[j].k * line[l].k + 1 == 0 | ((line[j].k - line[l].k) / (1 + line[j].k * line[l].k) - 1 == 0))){
						pass = false;
						break;
					}
				}
			}
		}
		if(pass){
			cout << "Yes" << endl;
		}
		else
			cout << "No" << endl;
	}
	return 0;
}