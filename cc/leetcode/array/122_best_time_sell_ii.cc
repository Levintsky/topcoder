class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n == 0)
            return 0;
        int res = 0;
        int buy = prices[0];
        for (int i = 1; i < n; ++i) {
            if (prices[i] > buy) 
                res += prices[i] - buy;                
            buy = prices[i];
        }
        return res;
    }
};