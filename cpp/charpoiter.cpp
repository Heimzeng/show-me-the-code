#include <iostream>
#include <cstring>
using namespace std;
int main(int argc, char const *argv[])
{
    // case 1 : 不能更改字符串内容，否则会报segmentation fault
    char* str = "helloworld";
    // str[0] = '1'; // 不允许
    // case 2 : 等价于case 1
    char* str2;
    str2 = "helloworld";
    // case 3 : 可以改写
    char* str3 = new char [11];
    strcpy(str3, str);
    cout << str3 << endl;
    return 0;
}
