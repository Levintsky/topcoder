class Solution {
public:
    unordered_map<string, vector<char> > memo;
    bool pyramidTransition(string bottom, vector<string>& allowed) {
        for (auto item : allowed) {
            memo[item.substr(0, 2)].push_back(item[2]);
        }
        return helper(bottom);
    }
    
    bool helper(string& s) {
        if (s.size() <= 1)
            return true;
        vector<string> res={""};
        vector<string> res2;
        int n = s.size();
        for (int i = 0; i < n-1; ++i) {
            if (memo.find(s.substr(i, 2)) == memo.end())
                return false;
            for (auto item : res) {
                for (auto newc : memo[s.substr(i, 2)])
                    res2.push_back(item + newc);
            } 
            swap(res, res2);
            res2.clear();
        }
        for (auto item : res) {
            if (helper(item))
                return true;
        }
        return false;
    }
};
