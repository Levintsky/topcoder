class Solution {
public:
    unordered_map<int, vector<int>> d2hour;
    unordered_map<int, vector<int>> d2minute;
    vector<string> readBinaryWatch(int num) {
        for (int i = 0; i < 12; ++i) {
            int c = count_one(i);
            if (c <= num) {
                if (d2hour.find(c) == d2hour.end()) {
                    vector<int> arr;
                    d2hour[c] = arr;
                }
                d2hour[c].push_back(i);
            }
        }
        for (int i = 0; i < 60; ++i) {
            int c = count_one(i);
            if (c <= num) {
                if (d2minute.find(c) == d2minute.end()) {
                    vector<int> arr;
                    d2minute[c] = arr;
                }
                d2minute[c].push_back(i);
            }
        }
        vector<string> result;
        for (int i = 0; i <= num; ++i) {
            if (d2hour.find(i) != d2hour.end() && d2minute.find(num-i) != d2minute.end()) {
                for (auto ii : d2hour[i]) {
                    for (auto jj : d2minute[num-i]) {
                        string tmp1 = to_string(ii);
                        string tmp2 = to_string(jj);
                        if (tmp2.size() == 1)
                            tmp2 = '0' + tmp2;
                        result.push_back(tmp1 + ":" + tmp2);
                    }
                }
            }
        }
        return result;
    }
    
    int count_one(int n) {
        int count = 0;
        int arr[6] = {1, 2, 4, 8, 16, 32};
        for (int i = 0; i < 6; ++i) {
            if ((arr[i] & n) > 0)
                count++;
        }
        return count;
    }
};
