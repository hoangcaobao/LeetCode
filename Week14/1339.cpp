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
// Segment tree concept
struct custom_TreeNode {
    long long sum;
    long long sum_left;
    long long sum_right;
    custom_TreeNode *left;
    custom_TreeNode *right;
    custom_TreeNode()
    {
        sum=0;
        sum_left=0;
        sum_right=0;
        left = NULL;
        right = NULL;
    }
};
class Solution {
public:
    void copy(TreeNode* root, custom_TreeNode* new_root){
        if(root==NULL){
            return;
        }
        
        new_root->left=new custom_TreeNode();
        new_root->right=new custom_TreeNode();
        copy(root->left, new_root->left);
        copy(root->right, new_root->right);
    }
    void build(TreeNode* root, custom_TreeNode* new_root){
        if(root==NULL){
            return;
        }
        if(root->left==NULL){
            new_root->sum_left=0;
        }
        if(root->right==NULL){
            new_root->sum_right=0;
        }
        build(root->left, new_root->left);
        build(root->right, new_root->right);
        new_root->sum= new_root->left->sum+new_root->right->sum+root->val;
        new_root->sum_left= new_root->left->sum;
        new_root->sum_right=new_root->right->sum;
    }
    void get_result(long long & result, TreeNode* root, custom_TreeNode* new_root,long long sum_of_all_nodes){
        if(root==NULL){
            return;
        }
        if(root->left==NULL){
            result=max((sum_of_all_nodes-new_root->right->sum)*new_root->right->sum, result);
        }
        else if(root->right==NULL){
            result=max((sum_of_all_nodes-new_root->left->sum)*new_root->left->sum, result);
        }
        else{
            result=max((sum_of_all_nodes-new_root->right->sum)*new_root->right->sum, result);
            result=max((sum_of_all_nodes-new_root->left->sum)*new_root->left->sum, result);
        }
         
        get_result(result, root->left, new_root->left, sum_of_all_nodes);
        get_result(result, root->right, new_root->right, sum_of_all_nodes);
    }
    int maxProduct(TreeNode* root) {
        struct custom_TreeNode* new_root=new custom_TreeNode();
        copy(root, new_root);
        build(root, new_root);
        long long sum_of_all_nodes=new_root->sum;
        long long result=0;
        get_result(result, root, new_root, sum_of_all_nodes);
        return result%1000000007 ;
    
    }
};
