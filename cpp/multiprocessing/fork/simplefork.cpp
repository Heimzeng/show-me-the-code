#include <unistd.h>
#include <stdlib.h>
#include <iostream>
using namespace std;
int main(int argc, char const *argv[])
{
	pid_t pid;
	pid = fork();
	if (pid == -1){
		cout << "fork error" << endl;
		exit(EXIT_FAILURE);
	}
	else if (pid == 0){
		auto mypid = getpid();
		auto parentpid = getppid();
		cout << "sonpid: " << mypid << endl;
		cout << "parentpid: " << parentpid << endl;
		cout << "son return: " << pid << endl;
	}
	else {
		cout << "parent return: " << pid << endl;
		auto parentpid = getpid();
		cout << "parentpid: " << parentpid << endl; 
	}
	exit(EXIT_SUCCESS);
	return EXIT_SUCCESS;
}