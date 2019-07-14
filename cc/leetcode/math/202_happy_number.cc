class Solution {
public:
    bool isHappy(int n) {
        if (n == 1)
            return true;
        unordered_set<int> s;
        while (s.find(n) == s.end()) {
            s.insert(n);
            int tmp = 0;
            while (n > 0) {
                tmp += pow(n % 10, 2);
                n /= 10;
            }
            n = tmp;
            if (n == 1)
                return true;
        }
        return false;
    }
};