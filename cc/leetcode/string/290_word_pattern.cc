class Solution {
public:
    unordered_map<char, string> p2s;
    unordered_map<string, char> s2p;
    bool wordPattern(string pattern, string str) {
        vector<string> arr;
        int i = 0;
        while (i < str.size()) {
            while (i < str.size() && str[i] == ' ')
                i++;
            if (i == str.size())
                break;
            int j = i;
            while (j < str.size() && str[j] != ' ')
                ++j;
            arr.push_back(str.substr(i, j-i));
            i = j + 1;
        }
        if (arr.size() != pattern.size())
            return false;
        for (i = 0; i < pattern.size(); ++i) {
            if (p2s.find(pattern[i]) == p2s.end()) {
                if (s2p.find(arr[i]) != s2p.end())
                    return false;
                p2s.insert({pattern[i], arr[i]});
                s2p.insert({arr[i], pattern[i]});
            } else {
                if (s2p.find(arr[i]) == s2p.end())
                    return false;
                if (s2p[arr[i]] != pattern[i])
                    return false;
                if (p2s[pattern[i]] != arr[i])
                    return false;
            }
        }
        return true;
    }
};