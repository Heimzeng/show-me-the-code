#include "Node.h"
#include "Node.cpp"

int main(int argc, char const *argv[])
{
    Node* root = new Node(0, 0);
    Node* left = new Node(1, 1);
    Node* right = new Node(2, 2);
    root -> left = left;
    root -> right = right;
    return 0;
}