class Solution {
public:
    int makeArrayIncreasing(vector<int>& arr1, vector<int>& arr2) {
        sort(arr2.begin(), arr2.end());
        
        // ith iteration:
        // dp[] maps potential last val to minimum ops to get to the val;
        unordered_map<int, int> dp1;
        dp1[-1] = 0;
        
        for (int item : arr1) {
            unordered_map<int, int> dp2;

            for (auto kv : dp1) {
                int k = kv.first, v = kv.second;
                // option 1: directly append (i+1)-th item at the end without ops
                if (item > k) {
                    if (dp2.find(item) == dp2.end())
                        dp2[item] = INT_MAX;
                    dp2[item] = min(dp1[k], dp2[item]);
                }
                // option 2: find the smallest valid in arr2 to replace it;
                auto new_it = upper_bound(arr2.begin(), arr2.end(), k);
                if (new_it != arr2.end()) {
                    int new_item = *new_it;
                    if (dp2.find(new_item) == dp2.end())
                        dp2[new_item] = INT_MAX;
                    dp2[new_item] = min(dp2[new_item], dp1[k]+1);
                }
            }
            swap(dp1, dp2);
            if (dp1.size() == 0)
                return -1;
        }
        // return min
        int res = INT_MAX;
        for (auto item : dp1)
            res = min(res, item.second);
        return res;
    }
};
