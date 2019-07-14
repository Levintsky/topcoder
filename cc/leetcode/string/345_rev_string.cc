class Solution {
public:
    unordered_set<char> ss = {'a','e','i','o','u','A','E','I','O','U'};
    string reverseVowels(string s) {
        int i = 0, j = s.length() - 1;
        while (i < j) {
            while (i < j && ss.find(s[i]) == ss.end())
                ++i;
            while (i < j && ss.find(s[j]) == ss.end())
                --j;
            swap(s[i], s[j]);
            ++i;
            --j;
        }
        return s;
    }
    
};