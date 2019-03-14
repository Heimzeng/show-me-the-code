#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> arr;
    string temp;
    while(cin >> temp) {
        cout << temp << endl;
        if (temp.find("\n"))
            break;
        arr.push_back(stoi(temp));
    }
    int N = arr.back();
    cout << N << endl;
    return 0;
}