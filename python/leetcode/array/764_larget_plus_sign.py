class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        if N == 0:
            return 0

        grid = self.generate_grid(N, 1)
        for i, j in mines:
            grid[i][j] = 0

        # left
        grid_l = self.generate_grid(N, 0)
        for i in range(N):
            for j in range(N):
                if j == 0 and grid[i][0] == 1:
                    grid_l[i][j] = 1
                elif grid[i][j] == 1:
                    grid_l[i][j] = grid_l[i][j-1] + 1
                else:
                    grid_l[i][j] = 0

        # right
        grid_r = self.generate_grid(N, 0)
        for i in range(N):
            for j in range(N-1, -1, -1):
                if j == N-1 and grid[i][j] == 1:
                    grid_r[i][j] = 1
                elif grid[i][j] == 1:
                    grid_r[i][j] = grid_r[i][j+1] + 1
                else:
                    grid_r[i][j] = 0

        # up
        grid_u = self.generate_grid(N, 0)
        for i in range(N):
            for j in range(N):
                if i == 0 and grid[i][j] == 1:
                    grid_u[i][j] = 1
                elif grid[i][j] == 1:
                    grid_u[i][j] = grid_u[i-1][j] + 1
                else:
                    grid_u[i][j] = 0

        # down
        grid_d = self.generate_grid(N, 0)
        for i in range(N-1, -1, -1):
            for j in range(N):
                if i == N-1 and grid[i][j] == 1:
                    grid_d[i][j] = 1
                elif grid[i][j] == 1:
                    grid_d[i][j] = grid_d[i+1][j] + 1
                else:
                    grid_d[i][j] = 0
        """
        print(grid_l)
        print(grid_r)
        print(grid_u)   
        print(grid_d)
        """

        max_ = 0
        for i in range(N):
            for j in range(N):
                item = min(grid_l[i][j], grid_r[i][j], grid_u[i][j], grid_d[i][j])
                max_ = max(item, max_)
        return max_

    def generate_grid(self, N, val):
        grid = []
        for i in range(N):
            grid.append([val] * N)
        return grid


if __name__ == "__main__":
    a = Solution()
    print(a.orderOfLargestPlusSign(5, [[4,2]]))
    print(a.orderOfLargestPlusSign(2, []))
    print(a.orderOfLargestPlusSign(1, [[0,0]]))
