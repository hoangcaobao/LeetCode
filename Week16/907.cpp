class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {
        vector<long long> dp(arr.size(), 0);
        vector<long long> result(arr.size(), 0);
        long long modulo=1000000007;
        dp[0]=arr[0];
        result[0]=arr[0];
        stack<pair<int, int>> s;
        s.push(make_pair(arr[0],0));
        for(int i=1; i<arr.size(); i++){
            int mark=-1;
            result[i]=result[i-1];
            while(!s.empty() and s.top().first>arr[i]){
                s.pop();
            }
            if(s.empty()){
                dp[i]+=(arr[i]*(i+1));
                dp[i]%=modulo;
            }
            else{
                dp[i]+=(arr[i]*(i-s.top().second));
                dp[i]%=modulo;
                dp[i]+=dp[s.top().second];
                dp[i]%=modulo;
            }
            result[i]+=dp[i];
            result[i]%=modulo;
            s.push(make_pair(arr[i],i));
        }
        
        return result[arr.size()-1];
    }
};
