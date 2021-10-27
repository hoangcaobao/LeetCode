class Solution {
public:
    int numOfWays(int n) {
        long long modulo=1000000007;
        vector<vector<long long>> dp(n+1, vector<long long> (3, 0) );
        // state 1 is two cells in 1 row is the same
        // state 2 is three cells in 1 row are different
        dp[1][1]=6;
        dp[1][2]=6;
        for(int i=2; i<=n; i++){
            dp[i][1]=(dp[i-1][1]*3+dp[i-1][2]*2);
            dp[i][2]=(dp[i-1][1]*2+dp[i-1][2]*2);
            dp[i][1]%=modulo;
            dp[i][2]%=modulo;
        }
        long long result=dp[n][1]+dp[n][2];
        result%=modulo;
        return result;
    }
};
