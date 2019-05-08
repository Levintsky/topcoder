"""
294. Flip Game II (Medium)

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Follow up:
Derive your algorithm's runtime complexity.
"""

"""
Solution 1: back-tracking with memo O(n!)
1. key point:
  str class in python is immutable
  s[i:i+2] = "++" is not correct!
"""

"""
Solution 2: Theory matters
Can we even do better than that? Sure! Below I'll show the time complexity can be reduced to O(N^2) using Dynamic Programming, but the improved method requires some non-trivial understanding of the game theory, and therefore is not expected in a real interview. If you are not interested, please simply skip the rest of the article:

Concept 1 (Impartial Game): Given a particular arrangement of the game
board, if either player have exactly the same set of moves should he
move first, and both players have exactly the same winning condition,
then this game is called impartial game. For example, chess is not
impartial because the players can control only their own pieces, and
the +- flip game, on the other hand, is impartial.

example 1: Nim-game (A1, A2, A3, ...)
Grundy number: the number of move to take to win?
can-take: [1,2,3]
g(0) = 0
g(1) = 1
g(2) = mex(g(1), g(0)) = mex(1, 0) = 2
g(3) = mex(g(2), g(1), g(0)) = mex(2, 1, 0) = 3
g(4) = mex(g(3), g(2), g(1)) = mex(3, 2, 1) = 0 (whatever you do, you will lose)
g(5) = mex(g(4), g(3), g(2)) = mex(0, 3, 2) = 1

example 2: Nim-game (2, 4, 6, 8)
op: divide by [2, 3, 6] and foor, until 0, no move can be taken
g(0) = 0
g(1) = 1
g(2) = mex(g(1), g(0)) = mex(1, 0) = 2
g(3) = mex(g(1), g(1), g(0)) = 2
g(4) = mex(2, 1, 0) = 3
g(6) = mex(g(3), g(2), g(1)) = 0
g(8) = mex(g(4), g(2), g(1)) = 0
for a game with 4 piles, (2, 4, 6, 8)
xor(g(2), g(4), g(6), g(8)) = xor(2, 3, 0, 0) = 1 != 0 (p1 can win)
feasible move:  move 4 -> 2 then:
  xor(g(2), g(2), g(6), g(8)) = xor(2, 2, 0, 0) = 0

Concept 1.1 Tic Tac Toe, Chess, ...

--

Concept 2 (Normal Play vs Misere Play): If the winning condition of
the game is that the opponent has no valid moves, then this game is
said to follow the normal play convention; if, alternatively, the
winning condition is that the player himself has no valid moves, then
the game is a Misere game. Our +- flip has apprently normal play.

Now we understand the the flip game is an impartial game under normal play. Luckily, this type of game has been extensively studied. Note that our following discussion only applies to normal impartial games.

In order to simplify the solution, we still need to understand one more concept:

Concept 3 (Sprague-Grundy Function): Suppose x represents a particular
arrangement of board, and x_0, x_1, x_2, ... ,x_k represent the board
after a valid move, then we define the Sprague-Grundy function as:

 g(x) = FirstMissingNumber(g(x_0), g(x_1), g(x_2), ... , g(x_k)). 
where FirstMissingNumber(y) stands for the smallest positive number
that is not in set y. For instance, if g(x_0) = 0, g(x_1) = 0, g(x_k) =
2, then g(x) = FMV({0, 0, 2}) = 1.

Why do we need this bizarre looking S-G function? Because we can instantly decide whether 1P has a winning move simply by looking at its value. I don't want to write a book out of it, so for now, please simply take the following theorem for granted:

Theorem 1: If g(x) != 0, then 1P must have a guaranteed winning move
from board state x. Otherwise, no matter how 1P moves, 2P must then
have a winning move.

So our task now is to calculate g(board). But how to do that?
Let's first of all find a way to numerically describe the board.
Since we can only flip ++ to --, then apparently, 
we only need to write down the lengths of consecutive ++'s of length >= 2 to define a board.
For instance, ++--+-++++-+----- can be represented as (2, 4).

(2, 4) has two separate '+' subsequences.
Any operation made on one subsequence does not interfere with the state of the other.
Therefore, we say (2, 4) consists of two subgames: (2) and (4).

Okay now we are only one more theorem away from the solution. This is the last theorem. I promise:

Theorem 2 (Sprague-Grundy Theorem): The S-G function of game x = (s1,
s2, ..., sk) equals the XOR of all its subgames s1, s2, ..., sk. e.g.
g((s1, s2, s3)) = g(s1) XOR g(s2) XOR g(s3).

With the S-G theorem, we can now compute any arbitrary g(x).
If x contains only one number N (there is only one '+' subsequence), then

g(x) = FMV(g(0, N-2), g(1, N-3), g(2, N-4), ... , g(N/2-1, N-N/2-2));
     = FMV(g(0)^g(N-2), g(1)^g(N-3), g(2)^g(N-4)), ... g(N/2-1, N-N/2-2));
Now we have the whole algorithm:

Convert the board to numerical representation: x = (s1, s2, ..., sk)
Calculate g(0) to g(max(si)) using DP.
if g(s1)^g(s2)^...^g(sk) != 0 return true, otherwise return false.
Calculating g(N) takes O(N) time (N/2 XOR operations plus the O(N) First Missing Number algorithm). And we must calculate from g(1) all the way to g(N). So overall, the algorithm has an O(N^2) time complexity.

Naturally, the code is bit more complicated than the backtracking version. But it reduces the running time from ~128ms to less than 1ms. The huge improvement is definitely worth all the hassle we went through:

int firstMissingNumber(unordered_set<int> lut) {
    int m = lut.size();
    for (int i = 0; i < m; ++i) {
        if (lut.count(i) == 0) return i;
    }
    return m;
}

bool canWin(string s) {
    int curlen = 0, maxlen = 0;
    vector<int> board_init_state;
    for (int i = 0; i < s.size(); ++i) {    
        if (s[i] == '+') curlen++;              // Find the length of all continuous '+' signs
        if (i+1 == s.size() || s[i] == '-') {
            if (curlen >= 2) board_init_state.push_back(curlen);    // only length >= 2 counts
            maxlen = max(maxlen, curlen);       // Also get the maximum continuous length
            curlen = 0;
        }
    }          // For instance ++--+--++++-+ will be represented as (2, 4)
    vector<int> g(maxlen+1, 0);    // Sprague-Grundy function of 0 ~ maxlen
    for (int len = 2; len <= maxlen; ++len) {
        unordered_set<int> gsub;    // the S-G value of all subgame states
        for (int len_first_game = 0; len_first_game < len/2; ++len_first_game) {
            int len_second_game = len - len_first_game - 2;
            // Theorem 2: g[game] = g[subgame1]^g[subgame2]^g[subgame3]...;
            gsub.insert(g[len_first_game] ^ g[len_second_game]);
        }
        g[len] = firstMissingNumber(gsub);
    }
    
    int g_final = 0;
    for (auto& s: board_init_state) g_final ^= g[s];
    return g_final != 0;    // Theorem 1: First player must win iff g(current_state) != 0
 }
"""


class Solution(object):
  def solve(self, s):
    if len(s) < 2: return False

    n = len(s)
    for i in range(n-1):
      if s[i:i+2] == "++":
        t = s[:i] + "--" + s[i+2:]
        if not self.solve(t):
          return True
    return False

  def solve2(self, s):
    self.memo = {}
    ret = self.helper(s)
    print(self.memo)
    return ret 

  def helper(self, s):
    n = len(s)
    if s not in self.memo:
      for i in range(n-1):
        if s[i:i+2] == "++":
          t = s[:i] + "--" + s[i+2:]
          if not self.helper(t):
            self.memo[s] = True
            return True
      self.memo[s] = False
    return self.memo[s]

  def canWin(self, s):
    """
    :type s: str
    :rtype: bool
    """
    curlen = 0
    maxlen = 0

    # board representation
    board = []
    for i in range(len(s)):
      if s[i] == '+':
        curlen += 1
      if i == len(s) - 1 or s[i] == '-':
        if curlen >= 2:
          board.append(curlen)
        maxlen = max(maxlen, curlen)
        curlen = 0

    # Sprague-Grundy function
    g = [0] * (maxlen + 1)
    for len_ in range(2, maxlen + 1):
      gsub = set()
      # logic: try all the combinations
      # if we can find a split into #first, #second
      # so that g(#first) ^ g(#second) == 0
      # then there will be no missing 0 in gsub
      for len_first in range(0, len_ // 2):
        len_second = len_ - len_first - 2
        print("first, second", len_first, len_second,
          g[len_first], g[len_second], g[len_first] ^ g[len_second])
        gsub.add(g[len_first] ^ g[len_second])
      print(len_, gsub)
      g[len_] = self.mex(gsub)
    print(g)

    # xor of all sub-games
    g_final = 0
    for item in board:
      g_final = g_final ^ g[item]
    return g_final != 0

  def mex(self, lut):
    # Mex short for: Mimumum Excludant
    # Given a g(x) = lut
    # return the first missing number in lut
    # if the first missing number != 0, p1 have a winning move from board x
    m = len(lut)
    for i in range(m):
      if i not in lut:
        return i
    return m

  def solve3(self, s):
    self.memo = {}
        
    def helper(s):
      if s in self.memo:
        return self.memo[s]
      for i in range(len(s)-1):
        if s[i:i+2] == "++":
          s = s[:i] + "--" + s[i+2:]
          if not helper(s):
            s = s[:i] + "++" + s[i+2:]
            self.memo[s] = True
            return True
          else:
            s = s[:i] + "++" + s[i+2:]
      self.memo[s] = False
      return False
    result = helper(s)
    # print(self.memo)
    return result

if __name__ == "__main__":
  a = Solution()
  # s = "+" * 4
  # print(s)
  print(a.canWin("++++-++++++++"))
  """  
  print(a.solve("+++++"))
  print(a.solve2("+++++"))
  for i in range(2, 50):
    s = "+" * i
    print(i, a.solve3(s))
  """