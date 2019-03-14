#ifndef NODE_H
#define NODE_H
class Node
{
public:
    Node(int key, int val);
    int key;
    int val;
    Node* left;
    Node* right;
};
#endif