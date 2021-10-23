class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if(amount==0){
            return 0;
        }
        vector<long long> dp (amount+1, INT_MAX);
        for(int i=0; i<coins.size(); i++){
            if(coins[i]<=amount){
                dp[coins[i]]=1;
            }
        }
        for(int i=1; i<=amount; i++){
            for(int j=0; j<coins.size(); j++){
                if(i>=coins[j]){
                    dp[i]=min(dp[i], dp[i-coins[j]]+1);
                }
            }
        }
        if(dp[amount]==INT_MAX){
            return -1;
        }
        return dp[amount];
    }
};
