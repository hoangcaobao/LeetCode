class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        set<string> sucess;
        for(int i=0; i<emails.size(); i++){
            int position=0;
            for(int j=0; j<emails[i].size(); j++){
                if(emails[i][j]=='@'){
                    position=j;
                }
            }
            string s="";
            for(int j=0; j<position; j++){
                if(emails[i][j]=='.'){
                    continue;
                }
                if(emails[i][j]=='+'){
                    break;
                }
                s+=emails[i][j];
            }
            s+=emails[i].substr(position, emails[i].size()-position);
            sucess.insert(s);
        }
        return sucess.size();
        
    }
};
