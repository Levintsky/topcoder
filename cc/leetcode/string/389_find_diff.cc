class Solution {
public:
    char findTheDifference(string s, string t) {
        array<int, 26> arr;
        fill(arr.begin(), arr.end(), 0);
        for (auto c : s)
            arr[c-'a']++;
        for (auto c : t) {
            arr[c-'a']--;
            if (arr[c-'a'] < 0)
                return c;
        }
        return 0;
    }
};
