class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> last;
        last.push_back({1});
        vector<int> next;
        
        for (int i = 1; i <= rowIndex; ++i) {
            next.resize(i+1, 1);
            for (int j = 1; j < i; ++j)
                next[j] = last[j-1] + last[j];
            swap(last, next);
        }
        return last;
    }
};