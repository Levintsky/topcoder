class Solution {
public:
    int sumSubarrayMins(vector<int>& A) {
        long MOD = 1e9 + 7;
        stack<pair<int, int>> s;
        long curr = 0, res = 0;
        for (int i = 0; i < A.size(); ++i) {
            int tmp_cnt = 1;
            long new_ = curr + A[i];
            while (s.size() > 0 && s.top().first >= A[i]) {
                auto old_item = s.top();
                s.pop();
                new_ -= (old_item.first - A[i]) * old_item.second;
                tmp_cnt += old_item.second;
            }
            s.push(make_pair(A[i], tmp_cnt));
            res = (res + new_) % MOD;
            curr = new_ % MOD;
        }
        return res;
    }
};
