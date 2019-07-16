class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        int n = deck.size();
        sort(deck.begin(), deck.end());
        queue<int> q; // for index
        for (int i = 0; i < n; ++i)
            q.push(i);
        vector<int> result(n, -1);
        int cnt = 0;
        while (q.size() > 0) {
            int i = q.front();
            q.pop();
            result[i] = deck[cnt];
            if (q.size() == 0)
                break;
            i = q.front();
            q.pop();
            q.push(i);
            cnt++;
        }
        return result;
    }
};
