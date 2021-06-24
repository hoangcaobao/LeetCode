class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        int check=0;
        int atleast=0;
        int already=0;
        for(int i=0; i<3; i++){
            already=0;
            for(int j=0; j<triplets.size(); j++){
                if(triplets[j][i]==target[i]){
                    if(already==0){
                        check+=1;
                        already=1;
                    }
                    if(i==0){
                        if (triplets[j][i+1]<=target[i+1]&&triplets[j][i+2]<=target[i+2] ){
                            atleast+=1;
                            break;
                        }
                    }
                    if(i==1){
                        if (triplets[j][i-1]<=target[i-1]&&triplets[j][i+1]<=target[i+1] ){
                            atleast+=1;
                            break;
                        }
                    }
                    if(i==2){
                        if (triplets[j][i-1]<=target[i-1]&&triplets[j][i-2]<=target[i-2] ){
                            atleast+=1;
                            break;
                        }
                    }
                    
                    
                }
            }
        }
        if(check==3 && atleast>=3){
            return true;
        }
        cout<<check<<atleast;
        return false;
    }
};
