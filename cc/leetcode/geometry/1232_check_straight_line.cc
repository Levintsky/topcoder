class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coord) {
        int x0 = coord[0][0], y0 = coord[0][1];
        int x1 = coord[1][0], y1 = coord[1][1];
        long dx1 = x1-x0, dy1 = y1 - y0;
        for (int i = 2; i < coord.size(); ++i) {
            long dx2 = coord[i][0] - x0;
            long dy2 = coord[i][1] - y0;
            if (dx1 * dy2 != dx2 * dy1)
                return false;
        }
        return true;
    }
};
