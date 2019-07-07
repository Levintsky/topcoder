"""
794. Valid Tic-Tac-Toe State (Medium)

A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is 
possible to reach this board position during the course of a valid tic-tac-toe 
game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true
Note:

board is a length-3 array of strings, where each string board[i] has length 3.
Each board[i][j] is a character in the set {" ", "X", "O"}.
"""

class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        m = len(board)
        if m != 3: return False
        for i in range(m):
            if len(board[i]) != 3:
                return False

        # check number of stones
        x, o = 0, 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == "X":
                    x += 1
                elif board[i][j] == "O":
                    o += 1
                elif board[i][j] != " ":
                    return False
        if x < o or x > o + 1:
            return False

        # check
        def count(c):
            # horizon
            res = 0
            for i in range(3):
                if board[i] == c * 3:
                    res += 1
                sub = "".join([board[j][i] for j in range(3)])
                if sub == c * 3:
                    res += 1
            if board[0][0] == board[1][1] == board[2][2] == c:
                res += 1
            if board[0][2] == board[1][1] == board[2][0] == c:
                res += 1
            return res

        cntx = count("X")
        cnto = count("O")
        if cntx * cnto > 0:
            return False
        if x == o and cntx > 0:
            return False
        if x == o + 1 and cnto > 0:
            return False
        return True


if __name__ == "__main__":
    a = Solution()
    print(a.validTicTacToe(["O  ", "   ", "   "]))
    print(a.validTicTacToe(["XOX", " X ", "   "]))
    print(a.validTicTacToe(["XXX", "   ", "OOO"]))
    print(a.validTicTacToe(["XOX", "O O", "XOX"]))
    print(a.validTicTacToe(["XOX", "OXO", "XOX"]))
    print(a.validTicTacToe(["XXX","XOO","OO "]))
