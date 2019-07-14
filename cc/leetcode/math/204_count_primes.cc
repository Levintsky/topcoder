class Solution {
public:
    int countPrimes(int n) {
        if (n < 2)
            return false;
        vector<bool> arr(n, true);
        arr[0] = false;
        arr[1] = false;
        int res = 0;
        for (int i = 2; i < n; ++i) {
            if (arr[i]) {
                res++;
                for (int j = 2; j * i < n; ++j)
                    arr[j * i] = false;
            } else
                continue;
        }
        return res;
    }
};