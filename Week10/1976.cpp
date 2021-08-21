class Solution {
public:
    long long find_min(vector<long long> &used, vector<long long> &dist, int &n){
        long long minn= LLONG_MAX;
        int min_index=INT_MAX;
        for(int i=0; i<n; i++){
            if(used[i]==0 && dist[i]<=minn){
                minn=dist[i];
                min_index=i;
            }
        }
        return min_index;
    }
    int countPaths(int n, vector<vector<int>>& roads) {
        map<long long, vector<pair<long long, long long>>>graph;
        for(int i=0; i<roads.size(); i++){
            graph[roads[i][0]].push_back(make_pair(roads[i][1], roads[i][2]));
            graph[roads[i][1]].push_back(make_pair(roads[i][0], roads[i][2]));
        }
        vector<long long> used(n+1, 0);
        vector<long long> dist(n+1, LLONG_MAX);
        vector<long long> count(n+1, 0);
        dist[0]=0;
        count[0]=1;
        
        while(true){
            int u=find_min(used, dist, n);
            if(u>=n){
                break;
            }
            used[u]=1;
            for(long long i=0; i<graph[u].size(); i++){
                if(used[graph[u][i].first]==0){
                    if(dist[graph[u][i].first]>dist[u]+graph[u][i].second){
                        dist[graph[u][i].first]=dist[u]+graph[u][i].second;
                        count[graph[u][i].first]=count[u];
                        count[graph[u][i].first]%=1000000007;
                    }
                    else if(dist[graph[u][i].first]==dist[u]+graph[u][i].second){
                        count[graph[u][i].first]+=count[u];
                        count[graph[u][i].first]%=1000000007;
                    }
                }
            }
        }
        return count[n-1];
        
    }
};
