class Solution {
public:
    void backtrack(vector<vector<int>> &result, vector<int> current, int pos, int previous, int n, int k){
        if(pos==k){
            result.push_back(current);
            return;
        }
        for(int i=previous+1; i<=n; i++){
            current.push_back(i);
            backtrack(result, current, pos+1, i, n,k);
            current.pop_back();
        }
    }
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> result;
        vector<int> current;
        backtrack(result, current, 0, 0, n, k);
        return result;
    }
};