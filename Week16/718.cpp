class Solution {
public:
    long long dp[1001][1001];
    int findLength(vector<int>& nums1, vector<int>& nums2) {
        for(int i=0; i<=nums1.size(); i++){
            dp[0][i]=0;
        }
        for(int i=0; i<=nums2.size(); i++){
            dp[i][0]=0;
        }
        long long result=0;
        for(int i=1; i<=nums2.size(); i++){
            for(int j=1; j<=nums1.size(); j++){
                if (nums1[j-1]==nums2[i-1]){
                    dp[i][j]=dp[i-1][j-1]+1;
                    result=max(result, dp[i][j]);
                }
                else{
                    dp[i][j]=0;
                }
            }
        }
        return result;
    }
};