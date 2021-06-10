class Solution {
public:
    void backtrack(vector<vector<int>> &result, vector<int> current, int current_sum, vector<bool> used, int pos, int n, int k){
        if(pos==k){
            if (current_sum==n){
                
                result.push_back(current);
            }
            return;
        }
        int start=1;
        if(current.size()!=0){
            start=current.back()+1;
        }
        for(int i=start; i<used.size(); i++){
            if(used[i]==false){
                used[i]=true;
                current.push_back(i);
                backtrack(result, current, current_sum+i, used, pos+1, n, k);
                used[i]=false;
                current.pop_back();
            }
        }
        
    }
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> result;
        vector<int> current;
        if(n>(9+9-k+1)*k/2){
           return result;
        } 
        vector<bool>used;
        for(int i=0; i<10; i++){
            used.push_back(false);
        }
        backtrack(result, current, 0, used, 0, n, k );
        return result;
    }
};