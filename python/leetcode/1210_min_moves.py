import collections


class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        visited = set()
        q = collections.deque()
        q.append((0, 1, 0))
        curr = 0
        while len(q) > 0:
            q2 = collections.deque()
            tmpset = set()
            while len(q) > 0:
                i, j, k = q.popleft()
                if i == n-1 and j == n-1 and k == 0:
                    return curr
                visited.add((i, j, k))
                if k == 0: # horizontal
                    if j < n-1 and grid[i][j+1] == 0: # go right
                        tmpset.add((i, j+1, 0))
                    if i < n-1 and grid[i+1][j-1] == 0 and grid[i+1][j] == 0:
                        tmpset.add((i+1, j, 0))
                    if i < n-1 and j > 0 and grid[i+1][j-1] == 0 and grid[i+1][j] == 0 and (i+1, j-1, 1) not in visited:
                        tmpset.add((i+1, j-1, 1))
                else: # vertical
                    if j < n-1 and grid[i-1][j+1] == 0 and grid[i][j+1] == 0:
                        tmpset.add((i, j+1, 1))
                    if i < n-1 and grid[i+1][j] == 0:
                        tmpset.add((i+1, j, 1))
                    if i > 0 and j < n-1 and grid[i-1][j+1] == 0 and grid[i][j+1] == 0 and (i-1, j+1, 0) not in visited:
                        tmpset.add((i-1, j+1, 0))
            for item in tmpset:
                q2.append(item)
            q = q2
            # print(curr, q2)
            curr += 1
        return -1


if __name__ == "__main__":
    a = Solution()
    print(a.minimumMoves([[0,0],[0,0]]))
    print(a.minimumMoves([[0,0,1],[0,0,0],[1,0,0]]))
    print(a.minimumMoves([[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]))
    print(a.minimumMoves([[0,0,1,1,1,1],
               [0,0,0,0,1,1],
               [1,1,0,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,0]]))
    print(a.minimumMoves([[0,0,0,0,0,0,0,0,0,1],
        [0,1,0,0,0,0,0,1,0,1],
        [1,0,0,1,0,0,1,0,1,0],
        [0,0,0,1,0,1,0,1,0,0],
        [0,0,0,0,1,0,0,0,0,1],
        [0,0,1,0,0,0,0,0,0,0],
        [1,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [1,1,0,0,0,0,0,0,0,0]]))
