class Solution {
public:
    unordered_map<string, pair<int, int>> memo;
    int mctFromLeafValues(vector<int>& arr) {
        int n = arr.size();
        auto result = helper(arr, 0, n-1);
        return result.second;
    }
    pair<int, int> helper(vector<int>& arr, int i, int j) {
        string key = to_string(i) + " " + to_string(j);
        if (memo.find(key) != memo.end())
            return memo[key];
        if (i == j)
            return make_pair(arr[i], 0);
        if (i + 1 == j) {
            memo[key] = make_pair(max(arr[i], arr[j]), arr[i]*arr[j]);
            return memo[key];
        }
        int max_ = INT_MIN, res = INT_MAX;
        for (int k=i; k < j; ++k) {
            auto tmp1 = helper(arr, i, k);
            auto tmp2 = helper(arr, k+1, j);
            int max1 = tmp1.first, max2 = tmp2.first;
            res = min(res, tmp1.second + tmp2.second + max1 * max2);
            max_ = max(max1, max2);
        }
        memo[key] = make_pair(max_, res);
        return memo[key];
    }
};

// Solution 2: faster, smarter
class Solution {
public:
    int mctFromLeafValues(vector<int>& arr) {
        stack<int> s;
        s.push(INT_MAX);
        int res = 0;
        for (auto item : arr) {
            while (item >= s.top()) {
                auto temp = s.top();
                s.pop();
                // if (!s.empty() && s.top() < item)
                //     res += temp * s.top();
                // else
                res += temp * min(item, s.top());
            }
            s.push(item);       
        }
        while (s.size() > 2) {
            auto temp = s.top();
            s.pop();
            res += s.top() * temp;
        }
        return res;
    }
};
