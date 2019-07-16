class Solution {
public:
    int tribonacci(int n) {
        vector<int> arr = {0, 1, 1};
        if (n < 3)
            return arr[n];
        for (int i = 2; i < n; ++i) {
            int tmp = arr[0] + arr[1] + arr[2];
            arr[0] = arr[1];
            arr[1] = arr[2];
            arr[2] = tmp;
        }
        return arr[2];
    }
};
