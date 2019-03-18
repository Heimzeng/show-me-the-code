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
    - 遍历每一个addr
    - 发送心跳包，设置一个timeout
    - 不回复则删除addr，以及停止对应线程/进程
    - 设置用户 状态
    - optional： 广播用户状态？
5. 锁帧
    - 服务器定时发送
    - 客户端没收到超过十个就锁定，直到接收到顺序帧
    - 客户端自己发出去的没收到10个之前的ack就锁定
    - 客户端收到空白帧，就锁定一帧
6. 多进程
    - 服务器分为tcp进程，udp进程、心跳进程和广播进程
    - 客户端有主进程，接收进程等
7. 靠谱的udp
    - 服务器resend未ack的前10个
    - 客户端不resend
8. 分包
    - 30秒的数据量就有10k，分为1包最大1k
9. 关键帧
    - 每10帧中间都会插入一个关键帧，客户端收到关键帧后立即同步所有玩家的状态
# sql

# user
1. password: bcrypt