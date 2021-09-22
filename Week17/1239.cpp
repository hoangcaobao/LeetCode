bool check_unique(string s){
    map<char, int> check;
    for(int i=0; i<s.size(); i++){
        if(check.find(s[i])!=check.end()){
            return false;
        }
        check[s[i]]=1;
    }
    return true;
}
void backtrack(vector<string>& arr, int position, string current, int &result){
    if(check_unique(current)==false){
        return;
    }
    if(current.size()>result){
        result=current.size();
    }
    if(position==arr.size()){
        return;
    }
    for(int i=position; i<arr.size(); i++){
        backtrack(arr, i+1, current+arr[i], result);
    }
    
}
class Solution {

public:
    int maxLength(vector<string>& arr) {
        int result=0;
        backtrack(arr, 0, "", result);
        return result;
    }
};
