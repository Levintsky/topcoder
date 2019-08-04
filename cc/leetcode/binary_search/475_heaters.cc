class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        sort(heaters.begin(), heaters.end());
        int best = 0;
        for (int h : houses) {
            auto tmp = lower_bound(heaters.begin(), heaters.end(), h);
            if (tmp == heaters.end())
                best = max(best, h - *(tmp-1));
            else if (*tmp == h)
                continue;
            else if (tmp == heaters.begin()) {
                best = max(best, *tmp - h);
            } else {
                int res = min(*tmp-h, h-*(tmp-1));
                best = max(best, res);
            }
        }
        return best;
    }
};
