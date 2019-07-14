class Solution {
public:
    string toHex(int num) {
        if (num == 0)
            return "0";
        bool neg_flag = num < 0;
        long num2 = num;
        if (num2 < 0)
            num2 = -num2;
        // make it hexadecimal
        vector<int> res;
        while (num2 > 0) {
            res.push_back(num2 % 16);
            num2 /= 16;
        }
        if (neg_flag) {
            while (res.size() < 8)
                res.push_back(0);
            for (int i = 0; i < 8; ++i)
                res[i] = 15 - res[i];
            res[0] += 1;
            if (res[0] == 16) {
                res[0] = 0;
                for (int i = 1; i < 8; ++i) {
                    if (res[i] == 15)
                        res[i] = 0;
                    else {
                        res[i]++;
                        break;
                    }
                }
            }
        }
        reverse(res.begin(), res.end());
        string result;
        for (auto item : res) {
            if (item < 10)
                result += '0' + item;
            else
                result += 'a' + item - 10;
        }
        return result;
    }
};
