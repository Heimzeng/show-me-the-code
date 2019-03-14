#include <iostream>
using namespace std;
class A
{
public:
	virtual void func(int val = 1){
		cout<<"A->"<<val<<endl;
	}
	virtual void test(){
		func();
	}
};
class B: public A
{
public:
	void func(int val){
		cout << "B->" << val << endl;
	}
};

int main(int argc, char const *argv[])
{
	B* p = new B;
	p->test();
	return 0;
}