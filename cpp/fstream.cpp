#include <iostream>
#include <fstream>
#include <string>

int main(int argc, char const *argv[])
{
    std::fstream fs;
    // char* filename = "./fstreamtest.txt";
    std::string filename = "./fstreamtest.txt";
    std::ios_base::openmode mode = std::ios_base::binary | std::ios_base::in;
    fs.open(filename, mode);
    if (fs.is_open())
        std::cout << "fstream opened" << std::endl;
    if (fs.good())
        std::cout << "fstream is good" << std::endl;
    return 0;
}