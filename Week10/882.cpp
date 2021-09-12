int find_min(vector<long long> & dis, vector<int> &used){
    int maxx=INT_MAX;
    int result=-1;
    for(int i=0; i<dis.size(); i++){
        if(maxx>=dis[i] && used[i]==0){
            maxx=dis[i];
            result=i;
        }
    }
    return result;
}
void dijkstra(map<int, vector<vector<int>>> &graph, vector<int> &used, vector<long long> &dis){
    while (true){
        int current=find_min(dis, used);
        cout<<current<<endl;
        if(current==-1){
            break;
        }
        used[current]=1;
        for(int i=0; i<graph[current].size(); i++){
            if(used[graph[current][i][0]]==0){
                dis[graph[current][i][0]]=min(dis[graph[current][i][0]],dis[current]+graph[current][i][1]);
                
            }
        }
    }
}
class Solution {
public:
    int reachableNodes(vector<vector<int>>& edges, int maxMoves, int n) {
        map<int, vector<vector<int>>> graph;
        for(int i=0; i<edges.size(); i++){
            graph[edges[i][0]].push_back({edges[i][1], edges[i][2]+1});
            graph[edges[i][1]].push_back({edges[i][0], edges[i][2]+1});
        }
        vector<long long> dis (n, INT_MAX);
        vector<int> used (n, 0);
        dis[0]=0;
        dijkstra(graph, used, dis);
        long long result=0;
        for(int i=0; i<n; i++){
            if(dis[i]<=maxMoves){
                result+=1;
            }
        }
        for(int i=0; i<edges.size(); i++){
            int left=maxMoves-dis[edges[i][0]];
            int right=maxMoves-dis[edges[i][1]];
            if(left<0){
                left=0;
            }
            if(right<0){
                right=0;
            }
            if(left+right>=edges[i][2]){
                result+=edges[i][2];
            }
            else{
                result+=(right+left);
            }
        }
        for(int i=0; i<n; i++){
            cout<<dis[i]<<" ";
        }
        return result;
        
    }
};
