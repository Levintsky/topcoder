class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        unordered_map<int, int> memo;
        int m = matrix.size();
        if (m == 0)
            return true;
        int n = matrix[0].size();
        if (n == 0)
            return true;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (memo.find(i-j) == memo.end()) {
                    memo[i-j] = matrix[i][j];
                } else {
                    if (matrix[i][j] != memo[i-j])
                        return false;
                }
            }
        }
        return true;
    }
};

// better solution
class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {

 
        for(int i=0;i<matrix.size()-1;i++)
        {
           for(int j=0;j<matrix[0].size()-1;j++)
           {
           if(matrix[i][j]!=matrix[i+1][j+1]) return false;//Only compare with 1 next element
           }      
         }
        return true;
    
    }
};
