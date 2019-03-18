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
5. 锁帧
    - 服务器定时发送
    - 客户端没收到超过十个就锁定，直到接收到顺序帧
    - 客户端自己发出去的没收到10个之前的ack就锁定
    - 客户端收到空白帧，就锁定一帧

# sql

# user
1. password: hash