#include <iostream>
#include <string>
using namespace std;

int main(){
    string strIn;
    cin >> strIn;
//    strIn = getline();
    long long N;
    cin >> N;
    for(long long i=0;i<N;i++){
	long long stepCount = 0;
	long long N, M, X, Y;
	cin >> N >> M >> X >> Y;
	long long j = 0;
	for(int j=0;;j++){
	    if(strIn[j] == 'u')
		X -= 1;
	    else if(strIn[j] == 'd')
		X += 1;
	    else if(strIn[j] == 'l')
		Y -= 1;
	    else if(strIn[j] == 'r')
		Y += 1;
	    else if(strIn[j] == '\0'){
		cout << stepCount << endl;
		break;
	    }
	    stepCount ++;
	    if(1<=X && X<=N && 1<=Y && Y<=M)
		continue;
	    else{
		cout << stepCount << endl;
		break;
	    }
	}
    }
    return 0;
}
