class Solution {
public:
    int getMaximumGold(vector<vector<int>>& grid) {
        int best = 0;
        int m = grid.size(), n = grid[0].size();
        vector<vector<bool>> memo;
        for (int i = 0; i < m; ++i) {
            memo.push_back(vector<bool>(n, true));
        }
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] > 0)
                    dfs(grid, memo, i, j, 0, best);
            }
        }
        return best;
    }
    
    void dfs(vector<vector<int>>& grid, vector<vector<bool>>& memo, int i, int j, int curr, int& best) {
        curr += grid[i][j];
        memo[i][j] = false;
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> diff = {{1,0},{-1,0},{0,1},{0,-1}};
        for (auto& tmpd : diff) {
            int di = tmpd[0], dj = tmpd[1];
            int ii = i+di, jj = j+dj;
            if (ii>=0 && ii < m && jj>=0 && jj < n && grid[ii][jj] > 0 && memo[ii][jj])
                dfs(grid, memo, ii, jj, curr, best);
        }
        best = max(best, curr);
        curr -= grid[i][j];
        memo[i][j] = true;
    }
};

class Solution {
    int m,n;
public:
    int dfs(vector<vector<int>> &grid,int i,int j){
        if(grid[i][j]==0) return 0;
        int result=0;
        int temp=grid[i][j];
        grid[i][j]=0;
        if(i>0) result=max(result,temp+dfs(grid,i-1,j));
        if(j>0) result=max(result,temp+dfs(grid,i,j-1));
        if(i<m-1) result=max(result,temp+dfs(grid,i+1,j));
        if(j<n-1) result=max(result,temp+dfs(grid,i,j+1));
        grid[i][j]=temp;
        return result;
    }
    int getMaximumGold(vector<vector<int>>& grid) {
        int result=0;
        m=grid.size();
        n=grid[0].size();
        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++)
                result=max(result,dfs(grid,i,j));   
        return result;
    }
};
