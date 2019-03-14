#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int getNums(vector<int> lines) {
    
}

int innerGetNums(vector<int> lines) {

}

int main(int argc, char const *argv[])
{
    int N;
    cin >> N;
    while (N--) {
        int M;
        cin >> M;
        vector<int> lines;
        while(M--) {
            int line;
            cin >> line;
            lines.push_back(line);
        }
        sort(lines.begin(), lines.end());
        cout << getNums(lines);
    }
    return 0;
}
