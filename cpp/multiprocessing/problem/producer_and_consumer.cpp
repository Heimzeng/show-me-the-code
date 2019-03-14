#include <atomic>
#include <mutex>
#include <iostream>
#include "semaphore.cpp"
#include <vector>
#include <thread>

using namespace std;

int buffersize = 10;
int producer_count = 1;
int consumer_count = 3;
//atomic<unsigned int> full(0);
//atomic<int> empty(buffersize);
semaphore full(0, 0, 10);
semaphore empty(10, 0, 10);
mutex dataLock;
vector<int> data;

void producer(){
    while(true){
        int data_to_produce = 10;
        if(empty.Down())
        {
            dataLock.lock();
            data.push_back(data_to_produce);
            cout << "producer " << std::this_thread::get_id() << " produced." << endl;
            cout << "buffer size: " << data.size() << endl;
            dataLock.unlock();
            full.Up(); 
        }
    }
}

void consumer(){
    while(true){
        if(full.Down()){
            dataLock.lock();
            auto data_to_consume = data.back();
            data.pop_back();
            cout << "consumer " << std::this_thread::get_id() << " consumed." << endl;
            cout << "buffer size: " << data.size() << endl;
            dataLock.unlock();
            empty.Up();
        }
    }
}

int main(int argc, char const *argv[])
{
    while(producer_count--){
        thread t(producer);
        t.detach();
    }
    consumer_count --;
    while(consumer_count--){
        thread t(consumer);
        t.detach();
    }
    thread t(consumer);
    t.join();
}