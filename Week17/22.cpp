class Solution {
public:
    bool check(string s){
        string stack;
        while(s.size()!=0){
            if(stack.size()==0){
                stack+=s[s.size()-1];
                s.pop_back();
            }
            else{
                if (stack[stack.size()-1]==')' && s[s.size()-1]=='('){
                    stack.pop_back();
                    s.pop_back();
                }
                else{
                    stack+=s[s.size()-1];
                    s.pop_back();
                }
            }
        }
        if (stack.size()==0){
            return true;
        }
        return false;
                    
    }
    void backtrack(vector<string> &result, map<string,int>count, string s, int pos, int n){
        if(pos==2*n){
            if (check(s)==true){
            result.push_back(s);
            }
            return;
        }        
        for(auto &i:count){
            if(i.second>0){
                i.second-=1;
                s=s+i.first;
                backtrack(result,count,s,pos+1,n);
                i.second+=1;
                s.pop_back();
            }
        }
    }
    vector<string> generateParenthesis(int n) {
        map<string,int>count;
        string s1;
        s1+='(';
        count[s1]=n;
        string s2;
        s2+=')';
        count[s2]=n;
        vector<string> result;
        backtrack(result,count,"",0,n);
        return result;
        
    }
};