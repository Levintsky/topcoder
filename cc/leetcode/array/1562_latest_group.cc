class Solution {
public:
    int findLatestStep(vector<int>& arr, int m) {
        int n = arr.size();
        vector<int> memo(n+2, 0); // memo of len
        int best = -1;
        int cnt_m = 0;
        for (int i = 0; i < n; ++i) {
            int item = arr[i];
            int len_l = memo[item-1];
            int len_r = memo[item+1];
            // merge
            if (len_l == m)
                cnt_m--;
            if (len_r == m)
                cnt_m--;
            int n_len = len_l + len_r + 1;
            memo[item-len_l] = n_len;
            memo[item+len_r] = n_len;
            if (n_len == m)
                cnt_m++;
            if (cnt_m > 0)
                best = i + 1;
        }
        return best;
    }
};
