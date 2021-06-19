const int MOD = 1e9 + 7;
class Solution {
public:
    int maxArea(int h, int w, vector<int>& horizontalCuts, vector<int>& verticalCuts) {
        sort(horizontalCuts.begin(), horizontalCuts.end());
        sort(verticalCuts.begin(),verticalCuts.end());
        long height=horizontalCuts[0];
        long width=verticalCuts[0];
        for(int i=1; i<horizontalCuts.size(); i++){
            height=max(height, (long) horizontalCuts[i]-horizontalCuts[i-1]);
        }
        for(int i=1; i<verticalCuts.size(); i++){
            width=max(width, (long)verticalCuts[i]-verticalCuts[i-1]);
        }
        
        height=max(height,(long)h-horizontalCuts[horizontalCuts.size()-1]);
        width=max(width, (long)w-verticalCuts[verticalCuts.size()-1]);
        return (height*width)%MOD;
    }
};
