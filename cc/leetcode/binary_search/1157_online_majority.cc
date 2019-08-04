class MajorityChecker {
public:
    unordered_map<int, vector<int>> memo;
    MajorityChecker(vector<int>& arr) {
        for (int i = 0; i < arr.size(); ++i) {
            memo[arr[i]].push_back(i);
        }
    }
    
    int query(int left, int right, int threshold) {
        for (auto &i : memo) {
            if (i.second.size() < threshold) continue;
            auto it1 = lower_bound(begin(i.second), end(i.second), left);
            auto it2 = upper_bound(begin(i.second), end(i.second), right);
            if (it2 - it1 >= threshold) return i.first;
          }
          return -1;
    }
};

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * MajorityChecker* obj = new MajorityChecker(arr);
 * int param_1 = obj->query(left,right,threshold);
 */
