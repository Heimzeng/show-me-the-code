//通过树的前序遍历和中序遍历，重建一颗完整的树
//未完善
#include <iostream>
#include <queue>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

int* findPosition(int* startInorder, int data){
    int* start = startInorder;
    while(start != NULL){
        if (*start == data)
            return start;
        start += 1;
    }
}

TreeNode* ConstructCore(int* startPreorder, int* endPreorder, int* startInorder, int* endInorder){
    TreeNode* root = new TreeNode(*startPreorder);
    int* position = findPosition(startInorder, *startPreorder);
    int leftTreeLength = position - startInorder;
    int rightTreeLength = endInorder - position;
    if (leftTreeLength > 0)
        root -> left = ConstructCore(startPreorder + 1, startPreorder + leftTreeLength, startInorder, startInorder + leftTreeLength - 1);
    if (rightTreeLength > 0)
        root -> right = ConstructCore(startPreorder + 1 + leftTreeLength, endPreorder, position + 1, endInorder);
    return root;
}

TreeNode* Construct(int* preorder, int* inorder, int length){
    if(preorder == NULL || inorder == NULL || length <= 0)
        return NULL;
    return ConstructCore(preorder, preorder + length - 1, inorder, inorder + length - 1);
}

//广度优先
void printATree(TreeNode* root){
    queue<TreeNode*> q;
    while(root){
        cout << root -> val << " ";
        if (root -> left)
            q.push(root -> left);
        if (root -> right)
            q.push(root -> right);
        if(q.empty())
            root = NULL;
        else{
            root = q.front();
            q.pop();
        }
    }
    cout << endl;
}

int main(int argc, char const *argv[])
{
    int preorder[8] = {1, 2, 4, 7, 3, 5, 6, 8, };
    int inorder[8] = {4, 7, 2, 1, 5, 3, 8, 6, };
    TreeNode* root = Construct(preorder, inorder, sizeof(preorder) / 4);
    printATree(root);
    return 0;
}