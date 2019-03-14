#include <iostream>
using namespace std;

void swap(int* a, int* b){
    int temp = *a;
    *a = *b;
    *b = temp;
    cout << "swap " << *a << " and " << *b << endl;
}

void quickSort(int* start, int* end){
    if(start >= end)
        return ;
    int pivot = *start;
    int* left = start;
    int* right = end;
    while(left < right){
        while(*right > pivot && left < right)
            right -= 1;
        while(*left <= pivot && left < right)
            left += 1;
        if(left == right)
            break;
        swap(left, right);
    }
    swap(left, start);
    quickSort(start, left - 1);
    quickSort(left + 1, end);
}

void print(int* arr, int len){
    while(len--){
        cout << *arr << " ";
        arr += 1;
    }
    cout << endl;
}

int main(int argc, char const *argv[])
{
    int numList[10] = {6, 1, 2, 7, 9, 3, 4, 5, 10, 8, };
    quickSort(numList, numList + 9);
    print(numList, 10);
    return 0;
}