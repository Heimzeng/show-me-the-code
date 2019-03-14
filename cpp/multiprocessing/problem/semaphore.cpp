#include <mutex>
using namespace std;
class semaphore
{
public:
    semaphore(int val, int min, int max){
        semaphore_num = val;
        this->min = min;
        this->max = max;
    }
    bool Up(){
        lock.lock();
        bool flag = false;
        if (semaphore_num + 1 <= max){
            semaphore_num += 1;
            flag = true;
        }
        lock.unlock();
        return flag;
    }
    bool Down(){
        lock.lock();
        bool flag = false;
        if (semaphore_num - 1 >= min){
            semaphore_num -= 1;
            flag = true;
        }
        lock.unlock();
        return flag;
    }
private:
    mutex lock;
    int semaphore_num;
    int min;
    int max;
};