#include <iostream>
using namespace std;

struct Point {

    int x;
    int y;
};

int main(int argc, char const *argv[])
{
    int N, M;
    cin >> N >> M;
    Point ends[N];
    Point begins[M];
    Point maxPoint;
    Point minPoint;

    for (auto i=0;i<N;i++) {
        int x, y;
        cin >> x >> y;
        Point p;
        p.x = x;
        p.y = y;
        ends[i] = p;
    }
    for (auto i=0;i<M;i++) {
        int x, y;
        cin >> x >> y;
        Point p;
        p.x = x;
        p.y = y;
        begins[i] = p;
    }
    
    for (auto i=0;i<M;i++) {
        int result = 0;
        Point p = begins[i];
        int x = p.x;
        int y = p.y;
        for (auto j=0;j<N;j++) {
            Point q = ends[j];
            int qx = q.x;
            int qy = q.y;
            result += abs(x - qx);
            result += abs(y - qy);
        }
        cout << result << endl;
    }
    return 0;
}