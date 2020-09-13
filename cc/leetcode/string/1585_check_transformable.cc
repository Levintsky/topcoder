class Solution {
public:
    bool isTransformable(string s, string t) {
        vector<deque<int>> qs;
        for (int i = 0; i < 10; ++i) {
            deque<int> tmp;
            qs.push_back(tmp);
        }
        
        for (int i = 0; i < s.size(); ++i) {
            int idx = s[i] - '0';
            qs[idx].push_back(i);
        }
        
        for (char c : t) {
            int idx = c - '0';
            if (qs[idx].size() == 0)
                return false;
            for (int i = 0; i < idx; ++i) {
                if (qs[i].size() > 0 && qs[i].front() < qs[idx].front())
                    return false;
            }
            qs[idx].pop_front();
        }
        return true;
    }
};
