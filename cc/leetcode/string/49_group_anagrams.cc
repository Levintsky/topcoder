/*
49. Group Anagrams (Medium)

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
*/

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> m;
        for (auto s : strs) {
            // get key
            string t = s;
            sort(t.begin(), t.end());
            m[t].push_back(s);
        }
        
        vector<vector<string>> res;
        for (auto x : m) {
            vector<string> tmp;
            for (auto item : x.second)
                tmp.push_back(item);
            res.push_back(tmp);
        }
        return res;
    }
};