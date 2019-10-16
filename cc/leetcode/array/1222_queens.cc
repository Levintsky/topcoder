class Solution {
public:
    string pair2string(int i, int j) {
        return to_string(i) + " " + to_string(j);
    }
    
    vector<vector<int>> queensAttacktheKing(vector<vector<int>>& queens, vector<int>& king) {
        unordered_set<string> s;
        for (auto& vec : queens) {
            s.insert(pair2string(vec[0], vec[1]));
        }
        int i = king[0], j = king[1];
        vector<vector<int>> result;
        vector<vector<int>> direction={{-1, 0}, {1, 0}, {0, -1}, {0, 1}, {-1, -1}, {1, 1}, {-1, 1}, {1, -1}};
        for (auto& d : direction) {
            int di = d[0], dj = d[1];
            int tmpi = i, tmpj = j;
            while (tmpi >= 0 && tmpi < 8 && tmpj >=0 && tmpj < 8) {
                tmpi += di;
                tmpj += dj;
                if (s.find(pair2string(tmpi, tmpj)) != s.end()) {
                    result.push_back({tmpi, tmpj});
                    break;
                }
            }
        }
        return result;
    }
};
