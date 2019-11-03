class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        vector<int> memo = {0};
        for (int item : nums) {
            if (item % 2 == 0)
                memo.back() += 1;
            else
                memo.push_back(0);
        }
        int result = 0;
        for (int i=k; i< memo.size(); ++i)
            result += (memo[i] + 1) * (memo[i-k] + 1);
        return result;
    }
};
