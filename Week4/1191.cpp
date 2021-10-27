class Solution {
public:
    int kConcatenationMaxSum(vector<int>& arr, int k) {
        long long summ=0;
        long long max_prefix=0;
        long long max_suffix=0;
        long long modulo=1000000007;
        // use kadane algorithm
        long long current=0;
        long long maxx=0; 
        for(int i=0; i<arr.size(); i++){
            summ+=arr[i];
            summ%=modulo;
            max_prefix=max(max_prefix, summ);
            maxx=max(maxx, current);
            if(current+arr[i]<arr[i]){
                current=0;
            }
            current+=arr[i];
            current%=modulo;
        
        }
        maxx=max(maxx, current);
        summ=0;
        for(int i=arr.size()-1; i>=0; i--){
            summ+=arr[i];
            summ%=modulo;
            max_suffix=max(max_suffix, summ);
        }
        if(k==1){
            return maxx;
        }
        else if(summ<=0){
            return max((max_suffix+max_prefix)%modulo, maxx%modulo);
        }
        else{
            return max((k*summ)%modulo, (max_suffix+max(0,k-2)*summ+max_prefix)%modulo);
        }
    }
};
