class Solution {
public:
    string dayOfTheWeek(int day, int month, int year) {
        // 1971/1/0: Thu
        int days = 4;
        for (int i = 1971; i < year; ++i) {
            if (i % 4 == 0 && i != 2100)
                days = (days + 366) % 7;
            else
                days = (days + 365) % 7;
        }
        vector<int> m = {31,28,31,30,31,30,31,31,30,31,30,31};
        for (int i = 1; i < month; ++i) {
            days += m[i-1];
            if (i == 2 && year % 4 == 0 && year != 2100)
                days++;
            days %= 7;
        }
        days = (days + day) % 7;
        vector<string> memo = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
        return memo[days];
    }
};
