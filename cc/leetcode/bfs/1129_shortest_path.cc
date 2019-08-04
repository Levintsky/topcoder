class Solution {
public:
    vector<int> shortestAlternatingPaths(int n, vector<vector<int>>& red_edges, vector<vector<int>>& blue_edges) {
		vector<unordered_map<int, vector<int>>> memo(2);
        edgeToMemo(red_edges, memo[0]);
        edgeToMemo(blue_edges, memo[1]);
		
		vector<vector<int>> res(n, vector<int>(2, 2*n));
		res[0][0] = 0; // red
		res[0][1] = 0; // blue
		queue<pair<int, int>> q;
		q.push({0, 0}); // color
		q.push({0, 1}); // color
		while (q.size() > 0) {
			auto item = q.front();
			q.pop();
			int i = item.first, c = item.second;
			for (int j : memo[c][i]) {
				if (res[j][c] == 2 * n) {
					res[j][c] = res[i][1-c] + 1;
					q.push({j, 1 - c});
				}
			}
		}
		vector<int> final_res(n);
		for (int i = 0; i < n; ++i) {
			final_res[i] = min(res[i][0], res[i][1]);
			if (final_res[i] == 2 * n)
				final_res[i] = -1;
		}
		return final_res;
    }

    void edgeToMemo(vector<vector<int>>& edges, unordered_map<int, vector<int>>& memo) {
    	for (auto& tmp_edge : edges) {
    		memo[tmp_edge[0]].push_back(tmp_edge[1]);
    	}
    }
};