class Solution {
public:
    unordered_map<int, int> s1;
    unordered_map<int, int> s2;
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        helper(s1, nums1);
        helper(s2, nums2);
        if (s1.size() > s2.size())
            swap(s1, s2);
        vector<int> res;
        for (auto item : s1) {
            if (s2.find(item.first) != s2.end()) {
                int c = min(item.second, s2[item.first]);
                for (; c > 0; --c)
                    res.push_back(item.first);
            }
        }
        return res;
    }
    
    void helper(unordered_map<int, int>& s, vector<int>& arr) {
        for (auto item : arr) {
            if (s.find(item) == s.end()) {
                s.insert({item, 1});
            } else {
                s[item]++;
            }
        }
    }
};

// better solution
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> m;
        vector<int> result;
        for (int n : nums1) m[n]++;
        for (int n : nums2)
            if (m[n]-- > 0) result.push_back(n);
        return result;
    }
};