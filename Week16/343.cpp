class Solution {
public:
    int dp[59];
    int integerBreak(int n) {
        for(int i=1; i<=n; i++){
            dp[i]=i-1;
        }
        for(int i=3; i<=n; i++){
            for(int j = 2; j <= i-1; j++) {
                dp[i] = max(max(max(max(dp[i-j]*j,dp[i-j]*dp[j]),(i-j)*j),(i-j)*dp[j]),dp[i]);
            }
        }
        return dp[n];
    }
};