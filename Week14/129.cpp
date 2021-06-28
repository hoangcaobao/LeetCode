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
#include<bits/stdc++.h>
class Solution {
public:
    void get_data(vector<int> &contain , string current, TreeNode* root){
        if(root->left==NULL && root->right==NULL){
            
            int a=stoi(current+to_string(root->val));
            contain.push_back(a);
            return;
        }
        if(root->left==NULL){
            get_data(contain, current+to_string(root->val), root->right);
        }
        else if (root->right==NULL){
            get_data(contain, current+to_string(root->val), root->left);
        }
        else{
            get_data(contain, current+to_string(root->val), root->right);
            get_data(contain, current+to_string(root->val), root->left);
        }
    }
    int sumNumbers(TreeNode* root) {
        vector<int> contain;
        get_data(contain, "", root);
        int result=0;
        return result;
    }
};
