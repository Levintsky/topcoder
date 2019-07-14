class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> s1(nums1.begin(), nums1.end());
        unordered_set<int> s2(nums2.begin(), nums2.end());
        
        vector<int> res;
        if (s1.size() > s2.size())
            swap(s1, s2);
        for (auto item : s1) {
            if (s2.find(item) != s2.end())
                res.push_back(item);
        }
        return res;

    }
};
