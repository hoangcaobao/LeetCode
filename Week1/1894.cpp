class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        long long tong=0;
        for(int i=0; i<chalk.size(); i++){
            tong+=chalk[i];
        }
        k=(k%tong);
        tong=0;
        long long result=0;
        for(int i=0; i<chalk.size();i++){
            tong+=chalk[i];
            if(tong>k){
                result=i;
                break;
            }
        }
        return result;
        
    }
};
