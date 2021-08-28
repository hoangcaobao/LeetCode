class Solution {
public:
    void backtrack(int position, int &result, vector<string> & strs, string current, string &current_string){
      
        if(current!=""){
            int check=0;
            int count=0;
            for(int i=0; i<strs.size(); i++){
                if(count==0 && strs[i]==current_string){
                    count=1;
                    continue;
                }
                int j=0;
                for(int k=0; k<strs[i].size(); k++){
                    if(strs[i][k]==current[j]){
                        j+=1;
                    }
                    if(j==current.size()){
                        check=1;
                        break;
                    }
                }
                if(check==1){
                    break;
                }
                   
                
               
            }
        
            if(check==0){
                if(result<current_string.size()-position+current.size()){
                    result= current_string.size()-position+current.size();
                }
                return;
            }
        }
        if(position==current_string.size()){
            return; 
        }
        backtrack(position+1, result, strs, current+current_string[position], current_string);
        backtrack(position+1, result, strs, current, current_string);

        
    }
    int findLUSlength(vector<string>& strs) {
        int result=0;
        for(int i=0; i<strs.size(); i++){
            backtrack(0, result, strs, "", strs[i]);
            
        }
        if(result==0){
            return -1;
        }
        return result;
    }
};
