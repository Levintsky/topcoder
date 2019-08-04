class Solution {
public:
    int longestWPI(vector<int>& hours) {
        vector<int> arr = {0};
        unordered_map<int, int> memo;
        memo[0] = -1;
        int best = 0, n = hours.size();

        for (int i = 0; i < n; ++i) {
        	int tmp = array.back();
        	if (hours[i] > 8)
        		tmp++;
        	else
        		tmp--;
        	if (tmp > 0)
        		best = i+1;
        	if (memo.find(tmp-1) != memo.end())
        		best = max(best, i - memo[tmp-1]);
        	if (tmp <= 0 && memo.find(tmp) == memo.end())
        		memo[tmp] = i;
        	arr.push_back(tmp);
        }
        return best;
    }
};