class Solution {
public:
    int snakesAndLadders(vector<vector<int>>& board) {
        int n = board.size();
        
        // id to (i, j)
        unordered_map<int, pair<int, int>> memo;
        int flag = true; // forward?
        int inc = 1;
        for (int i = n-1; i >=0; i--) {
            if (flag) {
                for (int j = 0; j < n; j++)
                    memo[inc++] = make_pair(i, j);
            } else {
                for (int j = n-1; j >=0; j--)
                    memo[inc++] = make_pair(i, j);
            }
            flag = !flag;
        }
                
        // bfs
        vector<bool> visited(n*n+1, false);
        visited[1] = true;
        queue<int> q;
        q.push(1);
        int step = 0;
        while (q.size() > 0) {
            queue<int> q2;
            while (q.size() > 0) {
                int item = q.front();
                if (item == n * n)
                    return step;
                q.pop();
                for (int new_item=item+1; new_item <= min(item+6, n*n); new_item++) {
                    auto pair_ij = memo[new_item];
                    int i = pair_ij.first, j = pair_ij.second;
                    int new_item2;
                    if (board[i][j] == -1)
                        new_item2 = new_item;
                    else
                        new_item2 = board[i][j];
                    
                    if (!visited[new_item2]) {
                        visited[new_item2] = true;
                        q2.push(new_item2);
                    }
                }
            }
            step++;
            swap(q, q2);
        }
        return -1;
    }
};
