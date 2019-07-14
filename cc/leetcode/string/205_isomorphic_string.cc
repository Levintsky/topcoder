class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> s2t;
        unordered_map<char, char> t2s;
        if (s.size() != t.size())
            return false;
        for (int i = 0; i < s.size(); ++i) {
            char c1 = s[i];
            char c2 = t[i];
            if (s2t.find(c1) == s2t.end() && t2s.find(c2) == t2s.end()) {
                s2t.insert({c1, c2});
                t2s.insert({c2, c1});
            } else if (s2t.find(c1) != s2t.end() && t2s.find(c2) != t2s.end()){
                if (s2t[c1] != c2)
                    return false;
                if (t2s[c2] != c1)
                    return false;
            } else
                return false;
        }
        return true;
    }
};