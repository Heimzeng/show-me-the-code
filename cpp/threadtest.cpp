#include <iostream>
#include <thread>
#include <atomic>
// std::atomic<int> count;
int count;
void add() {
	for (auto i=0;i<10000;i++) {
		count ++;
		std::cout << count << std::endl;
	}
}

int main() {
	count = 0;
	std::thread t[10];
	for (auto i=0;i<10;i++)
		t[i] = std::thread(add);
	for (auto i=0;i<10;i++)
		t[i].join();
	return 0;
}
