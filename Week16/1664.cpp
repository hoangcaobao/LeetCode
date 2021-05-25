class Solution {
public:
    long dp1[100001];
    long dp2[100001];
    int waysToMakeFair(vector<int>& nums) {
        if (nums.size()==1){
            return 1;
        }
        if(nums.size()==0){
            return 0;
        }
        dp1[nums.size()-1]=nums[nums.size()-1];
        dp1[nums.size()-2]=nums[nums.size()-2];
        dp2[0]=nums[0];
        dp2[1]=nums[1];
        for(int i=nums.size()-3; i>=0; i--){
            dp1[i]=dp1[i+2]+nums[i];
        }
        for(int i=2; i<nums.size(); i++){
            dp2[i]=dp2[i-2]+nums[i];
        }
        int result=0;
        for(int i=0; i<nums.size(); i++){
            if(i==0){
                if(dp1[1]==dp1[2]){
                    result+=1;
                }
            }
            else if(i==nums.size()-1){
                if(dp2[nums.size()-2]==dp2[nums.size()-3]){
                    result+=1;
                }
            }
            else if(i==1){
                if(dp2[0]+dp1[3]==dp1[2]){
                    result+=1;
                }
            }
            else if(i==nums.size()-2){
                if(dp1[nums.size()-1]+dp2[nums.size()-4]==dp2[nums.size()-3]){
                    result+=1;
                }
            }
            else{
                if(dp1[i+2]+dp2[i-1]==dp1[i+1]+dp2[i-2]){
                    result+=1;
                }
            }
        }
        return result;
        
    }
};