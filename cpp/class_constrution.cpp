//测试能否通过 = 实现函数构造
#include <iostream>
using namespace std;
class A
{
private:
	int value;
public:
	A(int n){
		value = n;
	}
	int getValue(){
		return value;
	}
};

int main(){
	A a = 10;
	cout << a.getValue() << endl;
	return 0;
}