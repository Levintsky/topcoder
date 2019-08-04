class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        if (m == 0)
            return false;
        int n = matrix[0].size();
        if (n == 0)
            return false;
        int i = 0, j = m * n - 1;
        while (i <= j) {
            int mid = (i + j) / 2;
            // m to (r, c)
            int r = mid / n;
            int c = mid % n;
            if (matrix[r][c] == target)
                return true;
            else if (matrix[r][c] > target)
                j = mid - 1;
            else
                i = mid + 1;
        }
        return false;
    }
};
