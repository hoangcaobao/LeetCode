class Solution {
public:
    void backtrack(map<string, int> &result, map <string, int> count, string current, int n,int alo){
        if(current.size()==n){
            result[current]=1;
           
        }
        if(current.size()!=0){
            result[current]=1;
        }
        for(auto &i: count){
        
            if (i.second>0){
                current=current+i.first;
                
                i.second-=1;
                backtrack(result, count, current, n,alo);
                i.second+=1;
                current.pop_back();
            }
        }
    }
    int numTilePossibilities(string tiles) {
        map <string, int> count;
        for(int i=0; i<tiles.size(); i++){
            string c;
            c+=tiles[i];
            count[c]=0;
        }
        map <string, int> result;
        for(int i=0; i<tiles.size(); i++){
            string c;
            c+=tiles[i];
            count[c]+=1;
        }
        backtrack(result, count, "", tiles.size(),1);
        return result.size();
    }
};