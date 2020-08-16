class Solution {
public:
    int minOperations(int n) {
        // vector<int> arr;
        int sum = 0;
        for (int i = 0; i < n; ++i) {
            int item = 2 * i + 1;
            sum += item > n? item - n : n - item;
        }
        sum /= 2;
        return sum;            
    }
};
