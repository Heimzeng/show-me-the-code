#include <iostream>
#include <cstring>
using namespace std;
// 排序算法

// 动态数组
// 二维指针
// 二分法

// seg fault case 1: null ptr
char *sortSperaters(char *sps)
{
    int len = 0;
    char *orin = sps;
    while (*sps != '\0')
    {
        len += 1;
        sps++;
    }

    char *res = new char[len + 1];
    strcpy(res, orin);

    for (int i = 0; i < len - 1; i++)
    {
        for (int j = i + 1; j < len; j++)
        {
            if (res[i] > res[j])
            {
                char temp = res[i];
                res[i] = res[j];
                res[j] = temp;
            }
        }
    }
    return res;
}

bool binSearch(char c, char *str)
{
    int len = strlen(str);
    int low = 0, high = len - 1;
    while (low <= high)
    {
        int middle = (low + high) / 2;
        if (c == str[middle])
        {
            return true;
        }
        else if (c > str[middle])
        {
            low = middle + 1;
        }
        else if (c < str[middle])
        {
            high = middle - 1;
        }
    }
    return false;
}

int *getSubStrCount(char *str, char *speraters)
{
    int len = strlen(str);
    int *positions = new int[len]();
    for (int i = 0; i < len; i++)
    {
        char cur = str[i];
        if ((cur >= 'a' && cur <= 'z') || (cur >= 'A' && cur <= 'Z'))
        {
            continue;
        }
        else if (cur < speraters[0] && cur > speraters[strlen(speraters) - 1])
        {
            continue;
        }
        // 二分查找
        else
        {
            if (binSearch(cur, speraters))
            {
                positions[i] = 1;
            }
        }
    }
    return positions;
}

char **getSubStrings(char *str, int *positions, int size)
{
    int count = 0;
    for (int i = 0; i < size; i++)
    {
        if (positions[i] == 1)
        {
            count += 1;
        }
    }
    char **res = new char *[count];

    int low = 0, high = 0;
    count = 0;
    for (int i = 0; i <= size; i++)
    {
        if (positions[i] == 1 || i == size)
        {
            high = i - 1;
            char *sub = new char[high - low + 1];
            for (int j = 0; j < high - low + 1; j++)
            {
                sub[j] = str[j + low];
            }
            res[count] = sub;
            count += 1;
            low = high + 2;
            high = low;
        }
    }
    return res;
}

int main(int argc, char const *argv[])
{
    char *str = "hello,world;sysu.tencent's";
    char *speraters = ";,.";

    char *res = sortSperaters(speraters);

    int *positions = getSubStrCount(str, res);

    for (int i = 0; i < strlen(str); i++)
    {
        cout << positions[i];
    }
    cout << endl;

    char **ress = getSubStrings(str, positions, strlen(str));

    int count = 0;
    for (int i = 0; i < strlen(str); i++)
    {
        if (positions[i] == 1)
        {
            count += 1;
        }
    }

    for (int i = 0; i < count + 1; i++)
    {
        cout << ress[i] << endl;
    }

    return 0;
}
