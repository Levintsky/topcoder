class Solution {
public:
    bool check_ok(vector<int>& position, int diff, int m) {
        int res = 1;
        int curr = position[0];
        int n = position.size();
        for (int i = 1; i < n; ++i) {
            if (position[i] - curr >= diff) {
                res++;
                curr = position[i];
            }
        }
        return res >= m;
    }
    
    int maxDistance(vector<int>& position, int m) {
        int best = 0;
        sort(position.begin(), position.end());
        int n = position.size();
        int l = 1, r = (position[n-1]-position[0])/(m-1);
        
        while (l <= r) {
            int mid = l+(r-l)/2;
            if (check_ok(position, mid, m)) {
                best = max(best, mid);
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return best;
    }
};
