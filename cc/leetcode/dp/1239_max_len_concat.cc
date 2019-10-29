class Solution {
public:
    int maxLength(vector<string>& arr) {
        vector<string> arr_u;
        for (string& s : arr) {
            long k = 0;
            bool flag = true;
            for (char c : s) {
                long i = 1 << (c-'a');
                if ((i & k) != 0)
                    flag = false;
                k |= i;
            }
            if (flag)
                arr_u.push_back(s);
        }
        
        unordered_map<long, int> memo;
        memo[0] = 0;
        for (string& s : arr_u) {
            unordered_map<long, int> memo2;
            // encode s
            long k = 0;
            for (char c : s)
                k |= 1 << (c - 'a');
            // add back
            for (auto item : memo) {
                if ((item.first & k) == 0) {
                    long key = item.first | k;
                    if (memo2.find(key) == memo2.end())
                        memo2[key] = item.second + s.size();
                    else
                        memo2[key] = max(memo2[key], item.second+1);
                }
            }
            // merge memo and memo2;
            for (auto item : memo2) {
                if (memo.find(item.first) == memo.end())
                    memo[item.first] = item.second;
                else
                    memo[item.first] = max(memo[item.second], memo2[item.first]);
            }
        }
        
        // final result
        int final_res = 0;
        for (auto& item: memo)
            final_res = max(final_res, item.second);
        return final_res;
    }
};
