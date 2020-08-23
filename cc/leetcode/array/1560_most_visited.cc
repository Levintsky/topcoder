class Solution {
public:
    vector<int> mostVisited(int n, vector<int>& rounds) {
        vector<int> a(n+1, 0);
        int curr = rounds[0];
        for (int i = 1; i < rounds.size(); ++i) {
            int tmp = rounds[i];
            if (curr <= tmp) {
                for (int j = curr; j <= tmp; ++j)
                    a[j]++;
            } else {
                for (int j = curr; j <= n; ++j)
                    a[j]++;
                for (int j = 0; j <= tmp; ++j)
                    a[j]++;
            }
            curr = tmp + 1;
        }
        // find max
        int max_ = 0;
        for (int item : a)
            max_ = max(max_, item);
        vector<int> res;
        for (int i = 1; i <= n; ++i) {
            if (a[i] == max_)
                res.push_back(i);
        }
        return res;
    }
};
