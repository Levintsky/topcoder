class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> arr_s(26, 0);
        vector<int> arr_t(26, 0);
        for (auto c : s)
            arr_s[c-'a']++;
        for (auto c : t)
            arr_t[c-'a']++;
        return arr_s == arr_t;
    }
};