#include <atomic>
#include <iostream>
#include <thread>
#include <vector>
#include <algorithm>
#include <chrono>
#include <ctime>
#include <mutex>
using namespace std;

//global variables
auto plus_times = 1000000;
auto thread_count = 10;
auto waiting_counter = thread_count;
// example 1: non atomic
long long ordinary_counter = 0;
void ordinary_counter_add(){
    auto times = plus_times;
    while(times--){
        ++ ordinary_counter;
    }
    waiting_counter --;
}
//example 2: atomic int
static atomic<long long> atomic_counter(0);
void atomic_counter_add(){
    auto times = plus_times;
    while(times--){
        ++ atomic_counter;
    }
    waiting_counter --;
}
//example 3: atomic_flag with class
class example3Class
{
public:
    void vpp(){
        while (lock.test_and_set(std::memory_order_acquire));
        //自旋？
        value ++;
        lock.clear(std::memory_order_release);
    }
    int value = 0;
private:
    atomic_flag lock = ATOMIC_FLAG_INIT;
};
example3Class example3;
void example3_add(){
    auto times = plus_times;
    while(times--){
        example3.vpp();
    }
    waiting_counter --;
}
//example 4: atomic_flag without class
int example4value = 0;
atomic_flag example4lock = ATOMIC_FLAG_INIT;
void example4vpp(){
    // may have some problems?
    while (example4lock.test_and_set(std::memory_order_acquire));
    example4value ++;
    example4lock.clear(std::memory_order_release);
}
void example4_add(){
    auto times = plus_times;
    while(times--){
        example4vpp();
    }
    waiting_counter --;
}
//example 5: atomic class
class example5Class
{
public:
    example5Class(int val){
        value = val;
    }
    int value;
};
atomic<example5Class> atomic_example5(0);
void example5_add(){
    auto times = plus_times;
    while(times--){
        example5Class expected = atomic_example5.load(std::memory_order_relaxed);
        example5Class new_value(expected.value+1);
        while(!atomic_example5.compare_exchange_strong(expected, new_value)){
            //这行代码告诉我们不能照抄
            new_value.value = expected.value + 1;
        }
    }
    waiting_counter --;
}
//example 6: mutex try lock
mutex mtx;
long long example6value = 0;
void example6_add(){
    auto times = plus_times;
    while(times--){
        while (!mtx.try_lock());
        ++ example6value;
        mtx.unlock();
    }
    waiting_counter --;
}
//example 7: mutex lock
long long example7value = 0;
void example7_add(){
    auto times = plus_times;
    while(times--){
        mtx.lock();
        ++ example7value;
        mtx.unlock();
    }
    waiting_counter --;
}
//example 8: atomic big class and just update 1 value
class example8Class
{
public:
    example8Class(int val){
        value = val;
    }
    int value;
    int somethingelse;
    //不支持多于两个参数？
    //待解决
    //int somethingelse1;
};
atomic<example8Class> atomic_example8(0);
void example8_add(){
    auto times = plus_times;
    while(times--){
        example8Class expected = atomic_example8.load(std::memory_order_relaxed);
        example8Class new_value(expected.value+1);
        while(!atomic_example8.compare_exchange_strong(expected, new_value)){
            //这行代码告诉我们不能照抄
            new_value.value = expected.value + 1;
        }
    }
    waiting_counter --;
}
//main function
int main(int argc, char const *argv[])
{
    //run example 1
    auto start1 = std::chrono::system_clock::now();
    auto thread_counter = thread_count;
    waiting_counter = thread_count;
    while(thread_counter--){
        thread t(ordinary_counter_add);
        t.detach();
    }
    while(0!=waiting_counter);
    auto start2 = std::chrono::system_clock::now();
    std::chrono::duration<double> elapsed_seconds = start2-start1;
    cout << "Example 1 use " << elapsed_seconds.count() << "s" << endl;
    cout << "Result: " << ordinary_counter << endl;
    //cout << "Result: " + ordinary_counter << endl;  // this line will cause "Segmentation fault (core dumped)"
    //run example 2
    thread_counter = thread_count;
    waiting_counter = thread_count;
    while(thread_counter--){
        thread t(atomic_counter_add);
        t.detach();
    }
    while(0!=waiting_counter);
    auto start3 = std::chrono::system_clock::now();
    elapsed_seconds = start3-start2;
    cout << "Example 2 use " << elapsed_seconds.count() << "s" << endl;
    cout << "Result: " << atomic_counter << endl;
    //run example 3
    thread_counter = thread_count;
    waiting_counter = thread_count;
    while(thread_counter--){
        thread t(example3_add);
        t.detach();
    }
    while(0!=waiting_counter);
    auto start4 = std::chrono::system_clock::now();
    elapsed_seconds = start4-start3;
    cout << "Example 3 use " << elapsed_seconds.count() << "s" << endl;
    cout << "Result: " << example3.value << endl;
    //run example 4
    thread_counter = thread_count;
    waiting_counter = thread_count;
    while(thread_counter--){
        thread t(example4_add);
        t.detach();
    }
    while(0!=waiting_counter);
    auto start5 = std::chrono::system_clock::now();
    elapsed_seconds = start5-start4;
    cout << "Example 4 use " << elapsed_seconds.count() << "s" << endl;
    cout << "Result: " << example4value << endl;
    //run example 5
    thread_counter = thread_count;
    waiting_counter = thread_count;
    while(thread_counter--){
        thread t(example5_add);
        t.detach();
    }
    while(0!=waiting_counter);
    auto start6 = std::chrono::system_clock::now();
    elapsed_seconds = start6-start5;
    cout << "Example 5 use " << elapsed_seconds.count() << "s" << endl;
    cout << "Result: " << atomic_example5.load().value << endl;
    //run example 6
    thread_counter = thread_count;
    waiting_counter = thread_count;
    while(thread_counter--){
        thread t(example6_add);
        t.detach();
    }
    while(0!=waiting_counter);
    auto start7 = std::chrono::system_clock::now();
    elapsed_seconds = start7-start6;
    cout << "Example 6 use " << elapsed_seconds.count() << "s" << endl;
    cout << "Result: " << example6value << endl;
    //run example 7
    thread_counter = thread_count;
    waiting_counter = thread_count;
    while(thread_counter--){
        thread t(example7_add);
        t.detach();
    }
    while(0!=waiting_counter);
    auto start8 = std::chrono::system_clock::now();
    elapsed_seconds = start8-start7;
    cout << "Example 7 use " << elapsed_seconds.count() << "s" << endl;
    cout << "Result: " << example7value << endl;
    //run example 5
    thread_counter = thread_count;
    waiting_counter = thread_count;
    while(thread_counter--){
        thread t(example8_add);
        t.detach();
    }
    while(0!=waiting_counter);
    auto start9 = std::chrono::system_clock::now();
    elapsed_seconds = start9-start8;
    cout << "Example 8 use " << elapsed_seconds.count() << "s" << endl;
    cout << "Result: " << atomic_example8.load().value << endl;
    //exit
    return 0;
}

/* result
input:
auto plus_times = 1000000;
auto thread_count = 10;
output:
Example 1 use 0.0332507s
Result: 3852625
Example 2 use 0.169846s
Result: 10000000
Example 3 use 3.04154s
Result: 10000000
Example 4 use 2.51047s
Result: 10000000
Example 5 use 0.899613s
Result: 10000000
Example 6 use 4.07827s
Result: 10000000
Example 7 use 0.811196s
Result: 10000000
conclusion:
Example 3 is not acceptable
Example 4 is a little better but also unacceptable
阻塞比忙等快？
2、5、7 are ok
*/