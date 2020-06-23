class Solution {
public:
    string itoa(int item) {
        stringstream ss;
        ss << item;
        return ss.str();
    }
    
    vector<string> getFolderNames(vector<string>& names) {
        vector<string> res;
        unordered_map<string, int> memo;
        
        for (string item : names) {
            // case 1: not show
            if (memo.find(item) == memo.end()) {
                res.push_back(item);
            } else {
                int k = memo[item];
                string tmp = item + "(" + itoa(memo[item]) + ")";
                while (memo.find(tmp) != memo.end()) {
                    memo[item]++;
                    tmp = item + "(" + itoa(memo[item]) + ")";
                }
                memo[tmp] = 1;
                res.push_back(tmp);
            }
            memo[item] += 1;
        }
        return res;
    }
};
