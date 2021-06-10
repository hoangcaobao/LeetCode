class Solution {
public:
    void backtrack(vector<vector<int>> &result, vector<int> current, int target, int current_sum, vector<int> candidates, int previous){
        if(current_sum>target){
            return;
        }
        if(current_sum==target){
            result.push_back(current);
        }
        
        for(int i=previous; i<candidates.size(); i++){
            current.push_back(candidates[i]);
            backtrack(result, current, target, current_sum+candidates[i], candidates, i);
            current.pop_back();
        }
    }
        
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> current;
        backtrack(result, current, target, 0, candidates, 0);
        return result;
    }
};