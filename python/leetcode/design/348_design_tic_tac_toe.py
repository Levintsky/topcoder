"""
348. Design Tic-Tac-Toe (Medium)

Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

1. A move is guaranteed to be valid and is placed on an empty block.
2. Once a winning condition is reached, no more moves is allowed.
3. A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
Follow up:
Could you do better than O(n2) per move() operation?
"""

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.row1 = [0] * n
        self.row2 = [0] * n
        self.diag1 = [0, 0] 
        self.col1 = [0] * n
        self.col2 = [0] * n 
        self.diag2 = [0, 0] 

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if player == 1:
          self.row1[row] += 1
          self.col1[col] += 1
          if row == col:
            self.diag1[0] += 1
          if row + col == self.n - 1:
            self.diag1[1] += 1
          if self.row1[row] == self.n: return 1 
          if self.col1[col] == self.n: return 1 
          if self.diag1[0] == self.n: return 1 
          if self.diag1[1] == self.n: return 1 
        if player == 2:
          self.row2[row] += 1
          self.col2[col] += 1
          if row == col:
            self.diag2[0] += 1
          if row + col == self.n - 1:
            self.diag2[1] += 1
          if self.row2[row] == self.n: return 2 
          if self.col2[col] == self.n: return 2
          if self.diag2[0] == self.n: return 2 
          if self.diag2[1] == self.n: return 2 
        print self.row1, self.col1, self.row2, self.col2
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

if __name__ == "__main__":
    obj = TicTacToe(2)
    print obj.move(0,0,2)
    print obj.move(0,1,1)
    print obj.move(1,1,2)
    """
    print obj.move(0,0,1)
    print obj.move(0,2,2)
    print obj.move(2,2,1)
    print obj.move(1,1,2)
    print obj.move(2,0,1)
    print obj.move(1,0,2)
    print obj.move(2,1,1)
    """
