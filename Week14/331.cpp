class Solution {
public:
    struct TreeNode{
        int val;
        TreeNode *left;
        TreeNode *right;
        TreeNode(int x){
            val=x;
            left=NULL;
            right=NULL;
        }
    };
    void backtrack(bool &result, int &position, vector<string> &preorder, TreeNode* tree){
        position+=1;
        if(position>=preorder.size()){
            result=false;
            return;
        }
        if(preorder[position]=="#"){
            return;
        }
        tree = new TreeNode(stoi(preorder[position]));
        backtrack(result, position, preorder, tree->left);
        backtrack(result, position, preorder, tree->left);
    }
    bool isValidSerialization(string preorder) {
        
        stringstream ss(preorder);
        vector<string> a;
        while( ss.good() ){
            string substr;
            getline( ss, substr, ',' );
            a.push_back( substr );
        }
        
        bool result=true;
        TreeNode *tree=NULL;
        int position=-1;
        backtrack(result, position, a, tree);
        if(position<a.size()-1){
            return false;
        }
        return result;
    }
};
