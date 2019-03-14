#include <iostream>
#include <string>
using namespace std;
// void test()
// {
//     // test to ensure the ops of string
//     string a = "afefefe";
//     cout << a << endl;
//     string b = "";
//     for (auto i = 0; i < 3; i++)
//     {
//         b.push_back(a[i]);
//     }
//     cout << b << endl;
//     b.insert(b.begin(), '0');
//     cout << b.find('0', 0) << endl;
//     cout << b << endl;

// }
string solution(string str_in) {
    string res = "";
    for (auto iter = str_in.begin(); iter != str_in.end(); iter++)
    {
        int pos = str_in.find(*iter);
        if (str_in.find(*iter, pos+1) == string::npos) {
            // 不重复
            continue;
        }
        if (res.find(*iter) == string::npos)
        {
            // push 插入排序
            if (res.empty())
            {
                res.push_back(*iter);
            }
            else
            {
                for (auto i = res.begin(); i != res.end(); i++)
                {
                    if (i == res.begin() && (*i) > (*iter))
                    {
                        res.insert(i, (*iter));
                    }
                    else if (i == res.end()-1 && (*i) < (*iter)) {
                        res.insert(i+1, (*iter));
                    }
                    else if (((*i) < (*iter) && (*(i + 1)) > (*iter)))
                    {
                        res.insert(i+1, (*iter));
                    }
                }
            }
        }
    }
    return res;
}
int main()
{
    // test();
    string str_in;
    cin >> str_in;
    auto res = solution(str_in);
    cout << res << endl;
    return 0;
}