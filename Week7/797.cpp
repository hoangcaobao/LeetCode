class Solution {
public:
    void backtrack(vector<vector<int>> &result, vector<vector<int>> &graph, vector<int> &current, int n, int pos){
        current.push_back(pos);
        if(pos==n){
            result.push_back(current);
        }
        for(int i=0; i< graph[pos].size(); i++){
            backtrack(result, graph, current, n, graph[pos][i]);
            
        }
        current.pop_back();
        
    }
    
    
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<vector<int>> result;
        vector<int> current;
        backtrack(result, graph, current, graph.size()-1, 0);
        return result;
    }
};
