class Solution {
public:
    int primePalindrome(int N) {
        vector<int> tmp = {2, 3, 5, 7, 11};
        for (int item : tmp) {
            if (N <= item)
                return item;
        }
        // get left half length
        int ndigit = 0, tmpN = N;
        while (tmpN > 0) {
            ndigit++;
            tmpN /= 10;
        }
        ndigit /= 2;
        int start = pow(10, ndigit-1);
        for (; start < 9999; start++) {
            for (int mid = 0; mid < 10; ++mid) {
                // get number
                string left = to_string(start);
                string total = left + char(mid + '0');
                reverse(left.begin(), left.end());
                total += left;
                // cout << total << endl;
                long num = stoi(total);
                if (num < N)
                    continue;
                if (check_prime(num))
                    return num;
            }
        }
        return -1;
    }
    
    bool check_prime(long num) {
        long i = 2;
        while (i * i <= num) {
            if (num % i == 0)
                return false;
            else
                ++i;
        }
        return true;
    }
};
