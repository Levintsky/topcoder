class Solution {
public:
    bool isPerfectSquare(int num) {
        if (num <= 0)
            return false;
        else if (num == 1)
            return true;
        int l = 1, r = num;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (mid < num / mid)
                l = mid + 1;
            else if (mid == num / mid)
                return num % mid == 0;
            else
                r = mid - 1;
        }
        return num / l == l && num % l == 0;
    }
};


// faster solution: the long trick
class Solution {
public:
    bool isPerfectSquare(int num) {
        long x = num;
        while (x * x > num) {
            x = (x + num / x) >> 1;
        }
        return x * x == num;
    }
};