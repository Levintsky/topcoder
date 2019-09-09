class Solution {
public:
    int dietPlanPerformance(vector<int>& calories, int k, int lower, int upper) {
        int n = calories.size();
        if (n < k)
            return 0;
        // preprocess
        int cumsum = 0, result = 0;
        for (int i = 0; i < k; ++i)
            cumsum += calories[i];
        if (cumsum > upper)
            result++;
        else if (cumsum < lower)
            result--;
        for (int i = k; i < n; ++i) {
            cumsum += calories[i] - calories[i-k];
            if (cumsum > upper)
                result++;
            else if (cumsum < lower)
                result--;
        }
        return result;
    }
};
