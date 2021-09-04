void check(bool &result, vector<int> & p, int current, map<int, int> &locked){
    if(current==-1){
        return;
    }
    if(locked.find(current)!=locked.end()){
        result=false;
        return;
    }
    check(result, p, p[current], locked);
}
void check(bool &result, int current, map<int, int> &locked, map<int, vector<int>> &graph){
    if(locked.find(current)!=locked.end()){
        result=true;
        locked.erase(current);
    }
    for(int i=0; i<graph[current].size(); i++){
        check(result, graph[current][i], locked, graph);
    }
}
class LockingTree {
public:
    vector<int> p;
    map<int, int> locked;
    map<int, vector<int>> graph;
    LockingTree(vector<int>& parent) {
        p=parent;
        for(int i=0; i<parent.size(); i++){
            graph[parent[i]].push_back(i);
        }
    }
    
    bool lock(int num, int user) {
        if(locked.find(num)==locked.end()){
            locked[num]=user;
            return true;
        }
        return false;
    }
    
    bool unlock(int num, int user) {
        if(locked.find(num)!=locked.end() && locked[num]==user){
            locked.erase(num);
            return true;
        }
        return false;
    }
    
    bool upgrade(int num, int user) {
        bool result=true;
        check(result, p, num, locked);
        if(result==false){
            return false;
        }
        bool result1=false;
        check(result1, num, locked, graph);
        if(result1==false){
            return false;
        }
        locked[num]=user;
        return true;
        
    }
};

/**
 * Your LockingTree object will be instantiated and called as such:
 * LockingTree* obj = new LockingTree(parent);
 * bool param_1 = obj->lock(num,user);
 * bool param_2 = obj->unlock(num,user);
 * bool param_3 = obj->upgrade(num,user);
 */
