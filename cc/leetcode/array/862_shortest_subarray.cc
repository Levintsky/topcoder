class Solution {
public:
    int shortestSubarray(vector<int>& A, int K) {
        list<pair<int, int>> l;
        l.push_back(make_pair(-1, 0));
        int n = A.size();
        int best = n + 1;
        
        for(int i = 0; i < n; ++ i) {
            int tmp = l.back().second + A[i];
            while (l.size() > 0 && tmp - l.front().second >= K) {
                best = min(best, i - l.front().first);
                l.pop_front();
            }
            while (l.size() > 0 && l.back().second >= tmp)
                l.pop_back();
            l.push_back(make_pair(i, tmp));
        }
        if (best <= n)
            return best;
        else
            return -1;
    }
};
