#include <iostream>
#include <map>
using namespace std;

int main()
{
    int N;
    while (cin >> N)
    {
        map<int, int> positiveNums;
        map<int, int> negativeNums;
        int sum = 0;
        while (N--)
        {
            int tempNum;
            cin >> tempNum;
            sum += tempNum;
            if (tempNum > 0)
            {
                positiveNums.insert({tempNum, tempNum});
                // cout << "posadd";
            }
            else if (tempNum < 0)
            {
                negativeNums.insert({tempNum, tempNum});
                // cout << "negadd";
            }
        }
        int M;
        cin >> M;
        int maxPositiveM = 0;
        int maxNegativeM = 0;

        int M2 = M;

        auto iter = negativeNums.begin();
        while (iter != negativeNums.end() && M > 0)
        {
            maxNegativeM += iter->first;
            iter++;
            M--;
        }

        M = M2;

        if (!positiveNums.empty())
        {
            auto iter = positiveNums.end();
            iter--;
            while (iter != positiveNums.begin() && M > 0)
            {
                maxPositiveM += iter->first;
                iter--;
                M--;
            }
            if (M > 0)
                maxPositiveM += iter->first;
        }

        // cout << maxPositiveM << endl;
        // cout << maxNegativeM << endl;

        if (sum > 0)
        {
            // cout << "sumge0" << endl;
            // cout << maxNegativeM << endl;
            sum -= 2 * maxNegativeM;
            cout << sum << endl;
        }
        else if (sum < 0)
        {
            // cout << "sumle0" << endl;
            // cout << maxPositiveM << endl;
            // cout << "sum:" << sum << endl;
            sum -= 2 * maxPositiveM;
            cout << abs(sum) << endl;
        }
        else
        {
            if (abs(maxNegativeM) > abs(maxPositiveM))
            {
                cout << abs(sum - 2 * (maxNegativeM)) << endl;
            }
            else
            {
                cout << abs(sum - 2 * (maxPositiveM)) << endl;
            }
        }
    }
}