class Solution {
public:
    int countElements(vector<int>& arr) {
        int result = 0;
        vector<int> stat(1001);
        for (int item : arr)
            stat[item]++;
        
        for (int i = 0; i < 1000; ++i) {
            if (stat[i+1]>0)
                result += stat[i];
        }
        return result;
    }
};
