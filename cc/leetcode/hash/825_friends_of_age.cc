class Solution {
public:
    int numFriendRequests(vector<int>& ages) {
        sort(ages.begin(), ages.end());
        int iA = 1, iB = 0, n = ages.size();
        int res = 0;
        while (iA < n) {
            if (ages[iA] <= 14) {
                iA++;
                continue;
            }
            while (iB < iA && 2 * ages[iB] - 14 <= ages[iA])
                iB++;
            res += iA - iB;
            iA++;
        }
        // unequal
        unordered_map<int, int> memo;
        for (int item : ages)
            memo[item] += 1;
        for (auto item : memo) {
            int v = item.second;
            if (v > 1 && item.first > 14)
                res += v * (v-1) / 2;
        }
        return res;
    }
};
