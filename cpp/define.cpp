#include <iostream>
using namespace std;
#define P2P_SUPPORT

int main(int argc, char const *argv[])
{
#ifdef P2P_SUPPORT
    cout << "defined" << endl;
#else
    cout << "not defined" << endl;
#endif
    return 0;
}