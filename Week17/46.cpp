class Solution {
public:
    void backtrack(vector<int>&current, vector<vector<int>> &result, map<int,int>&check, int pos){ 
        if(pos==check.size()){
            result.push_back(current);
            return;
        }
        for(auto &i:check){
            if(i.second==1){
                i.second-=1;
                current.push_back(i.first);
                backtrack(current, result, check, pos+1);
                i.second+=1;
                current.pop_back();
            }
        }
        
    }
    vector<vector<int>> permute(vector<int>& nums) {
        map<int,int> check;
        for(int i=0; i<nums.size(); i++){
            check[nums[i]]=1;
        }
        vector<int> current;
        vector<vector<int>> result;
        backtrack(current, result, check, 0);
        return result;
    }
};