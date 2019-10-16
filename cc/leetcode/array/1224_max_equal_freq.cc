class Solution {
public:
    int maxEqualFreq(vector<int>& nums) {
        unordered_map<int, int> memo, memo_memo;
        int result = 0;
        
        for (int i = 0; i < nums.size(); ++i) {
            // update
            int item = nums[i];
            memo[item]++;
            // update memo_memo
            int c = memo[item];
            memo_memo[c]++;

            if (c > 1) {
                memo_memo[c-1]--;
                if (memo_memo[c-1] == 0)
                    memo_memo.erase(c-1);
            }
            
            // check satisfy
            int min_key = INT_MAX, max_key = INT_MIN;
            for (auto item : memo_memo) {
                min_key = min(min_key, item.first);
                max_key = max(max_key, item.first);
            }
            // case 1: [1, 1, 2, 2, 3, 3, 3]
            if (min_key == max_key - 1 && memo_memo[max_key] == 1)
                result = i + 1;
            // case 2: [1, 1, 2, 2, 3, 3, k]
            if (min_key == max_key && i != nums.size() - 1)
                result = i + 2;
            // case 3: 
            if (min_key == 1 && memo_memo[1] == 1 && memo_memo.size() == 2)
                result = i + 1;
        }
        return result;
    }
};
