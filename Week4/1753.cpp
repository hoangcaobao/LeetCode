class Solution {
public:
    int maximumScore(int a, int b, int c) {
        priority_queue<int> pq;
        pq.push(a);
        pq.push(b);
        pq.push(c);
        int result=0;
        while(pq.size()>=2){
            int d=pq.top();
            pq.pop();
            int e=pq.top();
            pq.pop();
            result+=1;
            d-=1;
            e-=1;
            if(d>0){
                pq.push(d);
            }
            if(e>0){
                pq.push(e);
            }
        }
        return result;
    }
};
