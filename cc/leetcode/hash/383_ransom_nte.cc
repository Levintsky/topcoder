class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> r(26, 0);
        vector<int> m(26, 0);
        helper(ransomNote, r);
        helper(magazine, m);
        for (int i = 0; i < 26; ++i) {
            if (r[i] > m[i])
                return false;
        }
        return true;
    }
    
    void helper(string& s, vector<int>& cnt) {
        for (auto c: s)
            cnt[c-'a']++;
    }
};

// better solution: array<int>
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        array<int, 26> chars;
        std::fill(chars.begin(), chars.end(), 0);
        for (auto c : magazine)
        {
            chars[c-'a']++;
        }
        for (auto c : ransomNote)
        {
            chars[c-'a']--;
        }
        for (auto c : chars)
        {
            if (c < 0) return false;
        }
        return true;
    }
};
