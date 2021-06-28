/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void get_data(vector<int> &contain, TreeNode* root){
        if(root==NULL){
            return;    
        }
        get_data(contain, root->left);
        contain.push_back(root->val);
        get_data(contain, root->right);
    }
    TreeNode* create(vector<int> &contain, int start, int end){
        if(start>end){
            return NULL;
        }
        int mid=(start+end)/2;
        struct TreeNode* a= new TreeNode(contain[mid]);
        a->left=create(contain, start, mid-1);
        a->right=create(contain,mid+1, end);
        return a;
    }
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        vector<int> contain;
        get_data(contain, root);
        contain.push_back(val);
        sort(contain.begin(), contain.end());
        return create(contain, 0, contain.size()-1);
    }
};
