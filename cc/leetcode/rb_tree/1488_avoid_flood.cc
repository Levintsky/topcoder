class Solution {
public:
    vector<int> avoidFlood(vector<int>& rains) {
        vector<int> res;
        
        set<int> zeros;
        unordered_map<int, int> memo; // lake id -> day
        int n = rains.size();
        
        for (int i = 0; i < n; ++i) {
            int item = rains[i];
            if (item == 0) { // dry day
                zeros.insert(i);
                res.push_back(1);
            } else {
                if (memo.find(item) == memo.end()) {
                    // case 1: unused flood
                    res.push_back(-1);
                    memo[item] = i;
                } else {
                    // iterator of first index in zeros after pool item rains 
                    auto it = zeros.upper_bound(memo[item]);
                    if (it == zeros.end())
                        return {};
                    res[*it] = item;
                    zeros.erase(*it);
                    memo[item] = i;
                    res.push_back(-1);
                }
            }
        }
        return res;
    }
};
