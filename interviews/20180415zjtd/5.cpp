#include <iostream>
using namespace std;

int main(){
    int N;
    cin >> N;
    while(N--){
	int a, b, c;
	cin >> a >> b >> c;
	int min, max;
	if(a > b){
	    max = a;
	    min = b;
	}
	else{
	    max = b;
	    min = a;
	}
	if(c > max){
	    cout << 0 << endl;
	    continue;
	}
	else if(c == max || c == min){
	    cout << 1 << endl;
	    continue;
	}
	else if(c > min && c < max){
	    if (c % min == 0){
		cout << (c / min) << endl;
	    }
	    else{
		cout << 0 << endl;
	    }
	    continue;
	}
	else{
	    if(max % min == min % c){
		cout << ((max / min) + 1) * 2 << endl;
	    }
	    else{
		cout << 0 << endl;
	    }
	    continue;
	}
    }
    return 0;
}
