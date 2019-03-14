//计算二叉树的深度
#include <iostream>
#include <queue>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

int cal_tree_depth(TreeNode* root){
    if (root == NULL)
        return 0;
    int nLeft = cal_tree_depth(root -> left);
    int nRight = cal_tree_depth(root -> right);
    return (nLeft > nRight) ? nLeft + 1 : nRight + 1;
}

int main(int argc, char const *argv[])
{
    TreeNode* root = new TreeNode(1);
    root -> left = new TreeNode(2);
    root -> right = new TreeNode(3);
    root -> left -> left = new TreeNode(4);
    root -> left -> right = new TreeNode(5);
    root -> left -> right -> left = new TreeNode(7);
    root -> right -> right = new TreeNode(6);
    int depth = cal_tree_depth(root);
    cout << depth << endl;
    return 0;
}