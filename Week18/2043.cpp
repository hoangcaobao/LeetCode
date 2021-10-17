class Bank {
public:
    map<long long, long long> b;
    int maxx=0;
    Bank(vector<long long>& balance) {
        maxx=balance.size();
        for(long long i=0; i<balance.size(); i++){
            b[i+1]=balance[i];
        }
    }
    
    bool transfer(int account1, int account2, long long money) {
        if(money>b[account1]){
            return false;
        }
        if(account1<=0 || account1>maxx){
            return false;
        }
        if(account2<=0 || account2>maxx){
            return false;
        }
        b[account1]-=money;
        b[account2]+=money;
        return true;
    }
    
    bool deposit(int account, long long money) {
        if(account<=0 || account>maxx){
            return false;
        }
        b[account]+=money;
        return true;
    }
    
    bool withdraw(int account, long long money) {
        if(account<=0 || account>maxx){
            return false;
        }
        if(money>b[account]){
            return false;
        }
        b[account]-=money;
        return true;
    }
};

/**
 * Your Bank object will be instantiated and called as such:
 * Bank* obj = new Bank(balance);
 * bool param_1 = obj->transfer(account1,account2,money);
 * bool param_2 = obj->deposit(account,money);
 * bool param_3 = obj->withdraw(account,money);
 */
