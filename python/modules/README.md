# client
1. socket

# logger

# serializator
1. protobuf
2. optional： Huffman coding

# server
1. socket
2. multithreading or multiprocessing or epoll
3. reader writer lock, writer first
4. 心跳包 optional
    - 遍历每一个socket
    - 发送心跳包，设置一个timeout
    - 不回复则删除socket，以及停止对应线程/进程
    - 设置用户 状态
    - optional： 广播用户状态？


# sql

# user
1. password: hash