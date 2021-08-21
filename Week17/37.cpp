class Solution {
public:
    bool check_row(vector<vector<char>> & board, int i){
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
        return true;
    }
    bool check_column(vector<vector<char>> & board, int i){
       
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
        
        return true;
    }
    bool check_square(vector<vector<char>> & board, int x, int y){
        int i=0; 
        int j=0;
        if(x<3){
            i=0;
        }
        else if(x<6){
            i=1;
        }
        else{
            i=2;
        }
        if(y<3){
            j=0;
        }
        else if(y<6){
            j=1;
        }
        else{
            j=2;
        }
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
            
        return true;
    }

    void solve(vector<vector<char>> &result, vector<vector<char>> board, int position_x, int position_y){
        if(position_y==board[0].size()){
            if(position_x == board.size()-1){
                result=board;
                return;
            }
            solve(result, board, position_x+1,0);
        }
        else{
            if(board[position_x][position_y]!='.'){
                solve(result, board, position_x, position_y+1);
            }
            else{
                for(int i=1; i<=9; i++){
                    char temp1='0'+i;
                    board[position_x][position_y]=temp1;
                    if(check_row(board, position_x)==false){
                        continue;
                    }
                    if(check_column(board, position_y)==false){
                        continue;
                    }
                    if(check_square(board, position_x, position_y)==false){
                        continue;
                    }
                    solve(result, board, position_x, position_y+1);
                    
                }
            }
        }
        
        
    }
    void solveSudoku(vector<vector<char>>& board) {
        vector<vector<char>> temp2=board;
        solve(board, temp2, 0, 0);
    }
};
