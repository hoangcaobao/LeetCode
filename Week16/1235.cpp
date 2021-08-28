bool sortFunc(const vector<int>& p1, const vector<int>& p2) {
     return p1[0] < p2[0];
 }
class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        vector<vector<int>> contain;
        int max_end=0;
        for(int i=0; i<startTime.size(); i++){
            contain.push_back({endTime[i], startTime[i], profit[i]});
            max_end=max(max_end, endTime[i]);
        }
        sort(contain.begin(), contain.end(), sortFunc);
        int last=0;
        vector<int> dp(max_end+1, 0);
        for(int i=0; i<contain.size(); i++){
            for(int j=last+1; j<=contain[i][0]; j++){
                dp[j]=max(dp[j-1], dp[j]);
            }
            dp[contain[i][0]]=max(dp[contain[i][1]]+contain[i][2], dp[contain[i][0]]);
            last=contain[i][0];
        }
        int maxx=0;
        for(int i=0; i<=max_end; i++){
            maxx=max(maxx, dp[i]);
        }
        return maxx;
    }
};
