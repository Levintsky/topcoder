class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int n = days.size();
        if (n == 0)
            return 0;
        priority_queue<pair<int, int> > q; // max-heap
        unordered_map<int, int> memo;
        q.push({0, 0});
        for (int i = 0; i < n; ++i) {
            if (days[i] > -q.top().second) {
                int tmpc = -q.top().first;
                q.push({-tmpc-costs[0], -days[i]});
                q.push({-tmpc-costs[1], -days[i]-6});
                q.push({-tmpc-costs[2], -days[i]-29});
                while (-q.top().second < days[i])
                    q.pop();
            }
            memo[days[i]] = -q.top().first;
        }
        return memo[days[n-1]];
    }
};

// better: O(n)
int mincostTickets(vector<int>& days, vector<int>& costs) {
  unordered_set<int> travel(begin(days), end(days));
  int dp[366] = {};
  for (int i = 1; i < 366; ++i) {
    if (travel.find(i) == travel.end()) dp[i] = dp[i - 1];
    else dp[i] = min({ dp[i - 1] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2]});
  }
  return dp[365];
}

// better: O(n)
int mincostTickets(vector<int>& days, vector<int>& costs, int cost = 0) {
  queue<pair<int, int>> last7, last30;
  for (auto d : days) {
    while (!last7.empty() && last7.front().first + 7 <= d) last7.pop();
    while (!last30.empty() && last30.front().first + 30 <= d) last30.pop();
    last7.push({ d, cost + costs[1] });
    last30.push({ d, cost + costs[2] });
    cost = min({ cost + costs[0], last7.front().second, last30.front().second });
  }
  return cost;
}
