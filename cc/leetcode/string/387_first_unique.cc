class Solution {
public:
    int firstUniqChar(string s) {
        array<int, 26> arr;
        fill(arr.begin(), arr.end(), 0);
        
        for (auto c : s)
            arr[c-'a']++;
        for (int i = 0; i < s.size(); ++i) {
            if (arr[s[i]-'a'] == 1)
                return i;
        }
        return -1;
    }
};
