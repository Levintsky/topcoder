class Solution {
public:
    int minReorder(int n, vector<vector<int>>& connections) {
        unordered_map<int, vector<pair<int, bool>>> memo;
        queue<int> q;
        for (auto v : connections) {
            int i = v[0], j = v[1];
            memo[i].push_back(make_pair(j, false));
            memo[j].push_back(make_pair(i, true));
        }
        
        q.push(0);
        unordered_set<int> s;
        int result = 0;
        while (q.size() > 0) {
            int idx = q.front();
            q.pop();
            s.insert(idx);
            
            for (auto item : memo[idx]) {
                if (s.find(item.first) != s.end())
                    continue;
                else {
                    q.push(item.first);
                    if (!item.second)
                        result++;
                }
            }
        }
        return result;
    }
};
