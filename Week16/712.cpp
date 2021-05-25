class Solution {
public:
    int dp[1002][1002];
    int minimumDeleteSum(string s1, string s2) {
        for(int i=0; i<1001; i++){
            for(int j=0; j<1001; j++){
                dp[i][j]=INT_MAX;
            }
        }
        dp[0][0]=0;
        for(int i = 1; i <= s1.size(); i++) {
            dp[i][0] = dp[i-1][0] + int(s1[i-1]); 
        }
        for(int i = 1; i <= s2.size(); i++) {
            dp[0][i] = dp[0][i-1] + int(s2[i-1]);
        }
    
        for(int i=1; i<=s1.size(); i++){
            for(int j=1; j<=s2.size(); j++){
                if(s1[i-1]==s2[j-1]){
                     dp[i][j] = min(dp[i][j], dp[i-1][j-1]); 
                }
                else{
                    dp[i][j] = min(dp[i][j], min(dp[i][j-1] + int(s2[j-1]), dp[i-1][j] + int(s1[i-1])));
                }
            }
        }
        return dp[s1.size()][s2.size()];
    }
};