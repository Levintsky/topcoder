class Solution {
public:
    int dayOfYear(string date) {
        vector<int> memo({31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31});
        // parse date
        string tmp;
        tmp = date.substr(0, 4);
        int y = stoi(tmp);
        tmp = date.substr(5, 2);
        int m = stoi(tmp);
        tmp = date.substr(8, 2);
        int d = stoi(tmp);
        if (y % 4 == 0 && y % 100 != 0)
            memo[1] = 29;
        if (y % 400 == 0)
            memo[1] = 29;
        int total = 0;
        for (int i = 0; i < m-1; ++i)
            total += memo[i];
        total += d;
        return total;
    }
};
