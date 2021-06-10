class Solution {
public:
    void backtrack(vector<string> &contain, string s, int pos){
        if(pos==s.size()){
            contain.push_back(s);
            return;
        }
    
        
            backtrack(contain, s, pos+1);
            if(65<=int(s[pos]) && int(s[pos])<=90){
                s[pos]=s[pos]+32;
                backtrack(contain, s, pos+1);
                s[pos]=s[pos]-32;
            }
            if(97<=int(s[pos]) && int(s[pos])<=122){
                s[pos]=s[pos]-32;
                backtrack(contain, s, pos+1);
                s[pos]=s[pos]+32;
            }
        
    }
    vector<string> letterCasePermutation(string s) {
        vector<string> result;
        backtrack(result, s, 0);
      
        
        return result;
    }
};