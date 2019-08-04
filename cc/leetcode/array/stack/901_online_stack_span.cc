class StockSpanner {
public:
    stack<pair<int, int>> data;
    StockSpanner() {
        
    }
    
    int next(int price) {
        int c = 1;
        while (data.size() > 0 && data.top().first <= price) {
            c += data.top().second;
            data.pop();
        }
        data.push({price, c});
        return c;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */
