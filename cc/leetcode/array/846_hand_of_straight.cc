class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int W) {
        if (hand.size() % W != 0)
            return false;
        sort(hand.begin(), hand.end());
        stack<int> s; // keep maximum
        unordered_map<int, int> memo;
        for (int item : hand) {
            if (s.size() == 0 || s.top() != item)
                s.push(item);
            memo[item] += 1;
        }
        while (s.size() > 0) {
            // get maximum
            while (s.size() > 0 and memo.find(s.top()) == memo.end())
                s.pop();
            if (s.size() == 0)
                return true;
            int tmp = s.top();
            for (; tmp > s.top()-W; tmp--) {
                if (memo.find(tmp) != memo.end()) {
                    memo[tmp] -= 1;
                    if (memo[tmp] == 0)
                        memo.erase(tmp);
                } else
                    return false;
            }
        }
        return true;
    }
};

// Smarter
bool isNStraightHand(vector<int> hand, int W) {
        map<int, int> c;
        for (int i : hand) c[i]++;
        for (auto it : c)
            if (c[it.first] > 0)
                for (int i = W - 1; i >= 0; --i)
                    if ((c[it.first + i] -= c[it.first]) < 0)
                        return false;
        return true;
    }
