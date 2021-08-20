class Solution {
public:
    bool check_row(vector<vector<char>> & board){
        for(int i=0; i<board.size(); i++){
            map<char, int> check;
            for(int j=0; j<board[0].size(); j++){
                if(board[i][j]=='.'){
                    continue;
                }
                if(check.find(board[i][j])!=check.end()){
                    return false;
                }
                check[board[i][j]]=1;
            }  
        }
        return true;
    }
    bool check_column(vector<vector<char>> & board){
        for(int i=0; i<board[0].size(); i++){
            map<char, int> check;
            for(int j=0; j<board.size(); j++){
                if(board[j][i]=='.'){
                    continue;
                }
                if(check.find(board[j][i])!=check.end()){
                    return false;
                }
                check[board[j][i]]=1;
            }  
        }
        return true;
    }
    bool check_square(vector<vector<char>> & board){
        for(int i=0; i<=2; i++){
            for(int j=0; j<=2; j++){
                map<char, int> check;
                for(int k=i*3; k<(i+1)*3;k++){
                    for(int z=j*3; z<(j+1)*3; z++){
                        if(board[k][z]=='.'){
                            continue;
                        }
                        if(check.find(board[k][z])!=check.end()){
                            return false;
                        }
                        check[board[k][z]]=1;
                    }
                }
            }
        }
        return true;
    }
    bool isValidSudoku(vector<vector<char>>& board) {
        bool check1=check_row(board);
        bool check2=check_column(board);
        bool check3=check_square(board);
     
        if((check1==false||check2==false)|| check3==false){
            return false;
        }
        return true;
    }
};
