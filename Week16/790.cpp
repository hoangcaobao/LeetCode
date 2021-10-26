class Solution {
public:
    int numTilings(int n) {
        vector<long long> dp (n+1, 0);
        long long modulo=1000000007;
        dp[0]=1;
        dp[1]=1;
        for(int i=2; i<=n; i++){
            dp[i]+=dp[i-1];
            dp[i]%=modulo;
            dp[i]+=dp[i-2];
            dp[i]%=modulo;
            for(int j=i-3; j>=0; j--){
                dp[i]+=(2*dp[j]);
                dp[i]%=modulo;
            }
        }
       
        return dp[n];
    }
};
