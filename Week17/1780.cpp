class Solution {
public:
    void backtrack(bool &result, int n, vector<int> number, int pos){
        
        if(n==0){
            result=true;
            return;
        }
        if(n<0){
            return;
        }
        if(pos==number.size()){
            return;
        }
        backtrack(result, n, number, pos+1);
        backtrack(result, n-pow(3,number[pos]), number, pos+1);
    }
    bool checkPowersOfThree(int n) {
        int maximum=log(n)/log(3);
        if (pow(3,maximum)==n){
            return true;
        }
        vector<int> number;
        for(int i=0; i<=maximum; i++){
            number.push_back(i);
        }
        bool result=false;
        backtrack(result,n,number, 0);
        return result;
    }
};