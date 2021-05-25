class Solution {
public:
    int dp[501];
    int largest(int start, int end, vector<int> arr ){
        int result=0;
        for(int i=start; i<=end; i++){
            result=max(result, arr[i]);
        }
        return result;
    }
 
    int arr1[501];
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        dp[0]=arr[0];
        for(int i=0; i<arr.size(); i++){
            arr1[i]=arr[i];
        }
         
        for(int i=1; i<arr.size(); i++){
            dp[i]=arr[i]+dp[i-1];
        }
        for(int i=1; i<arr.size(); i++){
            for (int j=k; j>=1; j--){
                if(i-j>=0){
                    dp[i]=max(dp[i],dp[i-j]+j*(*max_element(arr1+i-j+1, arr1+i+1)));
                }
                else if(i-j==-1){
                    dp[i]=max(dp[i],j*(*max_element(arr1+i-j+1, arr1 + i+1)));
                }
            }
        }
        return dp[arr.size()-1];
    }
};