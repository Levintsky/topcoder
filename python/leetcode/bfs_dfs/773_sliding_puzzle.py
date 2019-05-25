"""
773. Sliding Puzzle (Hard)

On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.

Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.

Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
Input: board = [[3,2,4],[1,5,0]]
Output: 14
Note:

board will be a 2 x 3 array as described above.
board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
"""

class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        # bfs
        target = ((1,2,3),(4,5,0))
        curr_ = [board]
        dis = 0
        visited = set()

        def copy_(list_):
            new = []
            for tmplist in list_:
                new.append([item for item in tmplist])
            return new

        def generate(table):
            for i in [0, 1]:
                for j in range(3):
                    if table[i][j] == 0:
                        i0, j0 = i, j
            result = []
            tmp = copy_(table)
            if i0 == 0:
                tmp[0][j0] = tmp[1][j0]
                tmp[1][j0] = 0
            else:
                tmp[1][j0] = tmp[0][j0]
                tmp[0][j0] = 0
            result.append(tmp)
            # left right
            if j0 != 0:
                tmp2 = copy_(table)
                tmp2[i0][j0] = tmp2[i0][j0-1]
                tmp2[i0][j0-1] = 0
                result.append(tmp2)
            if j0 != 2:
                tmp3 = copy_(table)
                tmp3[i0][j0] = tmp3[i0][j0+1]
                tmp3[i0][j0+1] = 0
                result.append(tmp3)
            return result

        # bfs
        while len(curr_) > 0:
            # visit everyone and mark visited
            new_ = set() # one step away
            while len(curr_) > 0:
                curr = curr_.pop()
                # if visited
                curr_key = tuple([tuple(item) for item in curr])
                visited.add(curr_key)
                if curr_key == target: return dis
                # add new new_.add()
                result = generate(curr)
                for tmp in result:
                    tmp_key = tuple([tuple(item) for item in tmp])
                    if tmp_key not in visited:
                        new_.add(tmp_key)
            dis += 1
            curr_ = list(new_)
            curr_ = [list([list(item2) for item2 in item]) for item in curr_]
        return -1