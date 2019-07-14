class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n == 0)
            return 0;
        int best_sell = 0;
        int best_buy = -prices[0];
        for (int i = 1; i < n; ++i) {
            best_sell = max(best_sell, prices[i] + best_buy);
            best_buy = max(best_buy, -prices[i]);
        }
        return best_sell;
    }
};