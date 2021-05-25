#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
   
    long long dp[5][100000];
    int countVowelStrings(int n) {
        
        for(int i=0; i<5; i++){
            dp[i][0]=1;
        }
        for(int i=1; i<n; i++){
            for(int j=0; j<5; j++){
                for(int z=0; z<=j; z++){
                    dp[j][i]+=dp[z][i-1];
                }
            }
        }
        long result=0;
        for(int i=0; i<5; i++){
            result+=dp[i][n-1];
        }
        return result;
        
    }
};