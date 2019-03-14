#include <iostream>
using namespace std;

long long GCD(long long a, long long b){
	long long left = 0;
	while(true){
		left = a % b;
		if (0 == left){
			return b;
		}
		else{
			a = b;
			b = left;
		}
	}
}

int main(int argc, char const *argv[])
{
	long long n;
	cin >> n;
	long long res = 1;
	for (long long i=1;i<=n;i++){
		if (i * 2 <= n)
			continue;
		long long gcd = GCD(i, res);
		if (1 == gcd){
			res *= i;
		}
		else{
			res /= gcd;
			res *= i;
		}
		if (res >= 987654321){
			res = res % 987654321;
		}
	}
	cout << res << endl;
	return 0;
}