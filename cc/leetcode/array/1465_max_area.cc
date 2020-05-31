class Solution {
public:
    int maxArea(int h, int w, vector<int>& horizontalCuts, vector<int>& verticalCuts) {
        sort(horizontalCuts.begin(), horizontalCuts.end());
        horizontalCuts.push_back(h);

        sort(verticalCuts.begin(), verticalCuts.end());
        verticalCuts.push_back(w);
        
        int max_h=horizontalCuts[0], max_w=verticalCuts[0];
        for (int i = 1; i < horizontalCuts.size(); i++)
            max_h = max(max_h, horizontalCuts[i]-horizontalCuts[i-1]);
        
        for (int i = 1; i < verticalCuts.size(); i++)
            max_w = max(max_w, verticalCuts[i]-verticalCuts[i-1]);
        
        long result = static_cast<long>(max_h) * static_cast<long>(max_w);
        long MOD = static_cast<long>(pow(10, 9) + 7);
        result %= MOD;
        return int(result);

    }
};
