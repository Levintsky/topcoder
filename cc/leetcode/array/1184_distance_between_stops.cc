class Solution {
public:
    int distanceBetweenBusStops(vector<int>& distance, int start, int destination) {
        int s = min(start, destination), e = max(start, destination);
        int res1 = 0, total = 0;
        for (int i = s; i < e; ++i)
            res1 += distance[i];
        for (int item : distance)
            total += item;
        int res2 = total - res1;
        return min(res1, res2);
    }
};
