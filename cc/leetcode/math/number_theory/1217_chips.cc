class Solution {
public:
    int minCostToMoveChips(vector<int>& chips) {
        int even = 0, odd = 0;
        for (int item : chips) {
            if (item % 2 == 1)
                odd++;
            else
                even++;
        }
        return min(odd, even);
    }
};
