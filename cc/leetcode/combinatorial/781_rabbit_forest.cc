class Solution {
public:
    int numRabbits(vector<int>& answers) {
        unordered_map<int, int> memo;
        for (int item : answers)
            memo[item] += 1;
        int res = 0;
        for (auto item : memo) {
            int k = item.first, v = item.second;
            res += (k+1) *((v-1)/(k+1)+1);
        }
        return res;
    }
};
