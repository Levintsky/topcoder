class Solution {
public:
    int minAreaRect(vector<vector<int>>& points) {
        auto& pts = points;
        const auto N = pts.size();
        
        unordered_map<int,unordered_set<int>> mx;
        for (auto& p : pts) {
            mx[p[0]].emplace(p[1]);
        }

        auto min_area {INT_MAX};        
        
        for (auto i1=0; i1<N-1; i1++) {
            auto& p1=pts[i1];
            auto x1=p1[0], y1=p1[1];
            for (auto i2=i1+1; i2<N; i2++) {
                auto& p2=pts[i2];
                auto x2=p2[0], y2=p2[1];
                
                if (x1==x2 || y1==y2) continue;
                if (mx[x1].count(y2) && mx[x2].count(y1)) {
                    auto area = abs(x1 - x2) * abs(y1-y2);
                    min_area = min(min_area, area);                    
                }
            }
        }
        
        return min_area==INT_MAX ? 0 : min_area;
    }
};
