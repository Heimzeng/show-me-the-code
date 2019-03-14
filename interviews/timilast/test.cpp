#include <iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    char* ps = new char(10);
    ps[0] = 'z';
    cout << ps[0] << endl;
    char* ps2 = "jkl";
    cout << ps2[0] << endl;
    *ps2 = 'h';
    cout << ps2[0] << endl;
    return 0;
}
