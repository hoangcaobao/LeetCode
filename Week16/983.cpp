class Solution {
public:
    
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int dp[366];    
        int index=0;
        dp[0]=0;
        for(int i=1; i<366; i++){
            dp[i]=1000000;
        }
        for(int i=1; i<366; i++){
            if (index < days.size() && days[index]==i){
                dp[i]=min(dp[i],dp[i-1]+costs[0]);
                index+=1;
            }
            else{
                dp[i]=dp[i-1];
            }
            if(i>=7){
                dp[i]=min(dp[i-7]+costs[1], dp[i]);
            }
            if(i>=30){
                dp[i]=min(dp[i-30]+costs[2],dp[i]);
            }
        }
        return dp[365];
        
    }
};