#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char const *argv[])
{
    vector<int> v;
    v.push_back(1);
    v.push_back(2);
    for (auto i=v.begin();i!=v.end();) {
        v.erase(i);
    }
    cout << v.size() << endl;
    cout << v.empty() << endl;
    cout << v[0] << endl;
    return 0;
}
