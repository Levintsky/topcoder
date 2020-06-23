class BIT {
public:
    BIT (int num) {
        n = num;
        arr.resize(n+1, 0);
    }
    void update(int i, int delta) {
        while (i <= n) {
            arr[i] += delta;
            i += i & (-i);
        }
    }
    int query(int i) {
        int res = 0;
        while (i > 0) {
            res += arr[i];
            i -= i & (-i);
        }
        return res;
    }
private:
    vector<int> arr;
    int n;
};

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        // 1. set and rank
        set<int> s;
        unordered_map<int, int> rank;
        for (int item : nums)
            s.insert(item);
        int i = 0;
        for (int item : s)
            rank[item] = i++;
        
        // 2. count
        BIT tree(s.size());
        vector<int> res;
        int n = nums.size();
        for (i = n-1; i >= 0; i--) {
            int tmp_r = rank[nums[i]];
            res.push_back(tree.query(tmp_r));
            tree.update(tmp_r+1, 1);
        }
        std::reverse(res.begin(), res.end());
        return res;
    }
};
