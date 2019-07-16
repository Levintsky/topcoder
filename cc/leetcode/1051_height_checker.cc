class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int> bucket(101, 0);
        for (auto item : heights)
            bucket[item]++;
        // accumulate comparison
        int start = -1, end = -1;
        int res = 0;
        for (int i = 0; i <= 100; ++i) {
            if (bucket[i] > 0) {
                start++;
                end = start + bucket[i] - 1;
                for (int j = start; j <= end; j++) {
                    if (heights[j] != i)
                        res++;
                }
                start = end;
            }
        }
        return res;
    }
};
