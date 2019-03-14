#include <iostream>
using namespace std;

struct A {
    char a;
    int b;
    float c;
};

struct B {
    char a;
};

struct C {
    char a;
    short b;
    int c;
};

struct D {

};

int main(int argc, char const *argv[])
{
    /* code */
    cout << sizeof(A) << endl;
    cout << sizeof(B) << endl;
    cout << sizeof(C) << endl;
    cout << sizeof(D) << endl;
    return 0;
}
