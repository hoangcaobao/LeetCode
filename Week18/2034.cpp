class StockPrice {
public:
    StockPrice() {
        
    }
    int minn=1;
    int maxx=1000000000;
    int lastest=0;
    map<pair<int, int>, int> save1;
    map<int, int> save2;
    void update(int timestamp, int price) {
        lastest=max(timestamp, lastest);
        if(save2[timestamp]!=0){
            save1.erase(make_pair(save2[timestamp], timestamp));
            save1[make_pair(price, timestamp)]=1;
            save2[timestamp]=price;
        }
        else{
            save1[make_pair(price, timestamp)]=1;
            save2[timestamp]=price;
        }
    }
    
    int current() {
        return save2[lastest];
    }
    
    int maximum() {
        return (--save1.end())->first.first; 
    }
    
    int minimum() {
        return save1.begin()->first.first;
    }
};

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice* obj = new StockPrice();
 * obj->update(timestamp,price);
 * int param_2 = obj->current();
 * int param_3 = obj->maximum();
 * int param_4 = obj->minimum();
 */
