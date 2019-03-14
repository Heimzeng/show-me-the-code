#include <iostream>
#include <string>
using namespace std;

string solution(string str_in)
{
    char most;
    int count_most = 0;
    if (str_in.empty())
        return "";
    auto iter = str_in.begin();

    char cur = *iter;
    int count_cur = 0;

    while (iter < str_in.end())
    {
        if (cur == *iter)
        {
            count_cur++;
        }
        else
        {
            if ((count_cur > count_most) || (count_cur == count_most && cur < most))
            {
                count_most = count_cur;
                most = cur;
            }
            cur = *iter;
            count_cur = 1;
        }
        iter++;
        if (iter == str_in.end())
        {
            if ((count_cur > count_most) || (count_cur == count_most && cur < most))
            {
                count_most = count_cur;
                most = cur;
            }
        }
    }

    string res = "";
    while (count_most--)
        res.push_back(most);

    return res;
}

int main()
{
    string str_in;
    cin >> str_in;
    string res = solution(str_in);
    cout << res << endl;
    return 0;
}