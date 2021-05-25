class Solution {
public:
    int dp[5001];
    int numberOfArithmeticSlices(vector<int>& nums) {
        for(int i=1; i<nums.size(); i++){
            dp[i]=nums[i]-nums[i-1];
        }
        
        int start=1;
        int result=0;
        for(int i=2; i<nums.size(); i++){
            if (dp[i]!=dp[i-1]){
                if (i+1-start>2){
                    result+=((i-start)*(i-start-1))/2;
                }
                start=i;
            }
        }
        if (nums.size()+1-start>2){
            result+=((nums.size()-start)*(nums.size()-start-1))/2;
        }
        return result;
    }
};