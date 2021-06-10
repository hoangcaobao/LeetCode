class Solution {
public:
    void backtrack(vector<string> &result, string current, int pos, int n, vector<char> &alphabet){
        if(pos==n){
            result.push_back(current);
            return;
        }
        for(int i=0; i<alphabet.size(); i++){
            if(pos==0){
                current=current+alphabet[i];
                backtrack(result, current, pos+1, n, alphabet);
                current.pop_back();
            }
            else if(alphabet[i]!=current[pos-1]){
                current=current+alphabet[i];
                backtrack(result, current, pos+1, n, alphabet);
                current.pop_back();
            }
        }
    }
    string getHappyString(int n, int k) {
        vector<char> alphabet {'a','b','c'};
        vector<string> result;
        backtrack(result, "", 0, n, alphabet);
        if (k>result.size()){
            return "";
        }
        sort(result.begin(), result.end());
        return result[k-1];
    }
};