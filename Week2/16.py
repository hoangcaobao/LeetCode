class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int result=0;
        int distance=INT_MAX;
        for(int i=0; i<nums.size()-2; i++){
            for(int j=i+1; j<nums.size()-1; j++){
                int tong=nums[i]+nums[j];
                int end=nums.size()-1;
                int start=j+1;
                while(start<=end){
                    int mid=(start+end)/2;
                    int check=tong+nums[mid];
                    if(check<target){
                        start=mid+1;
                        if(distance>abs(check-target)){
                            distance=abs(check-target);
                            result=check;
                        }
                    }
                    else{
                        end=mid-1;
                        if(distance>abs(check-target)){
                            distance=abs(check-target);
                            result=check;
                        }
                    }
                }
                
            }
        }
        return result;
    }
};
