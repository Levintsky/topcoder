"""
Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

Examples:

Input: "WRRBBW", "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW

Input: "WWRRBBWW", "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty

Input:"G", "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty 

Input: "RBYYBBRRB", "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty 

Note:
You may assume that the initial row of balls on the table won't have any 3 or more consecutive balls with the same color.
The number of balls on the table won't exceed 20, and the string represents these balls is called "board" in the input.
The number of balls in your hand won't exceed 5, and the string represents these balls is called "hand" in the input.
Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.
"""

"""
class Solution(object):
    def findMinStep(self, board, hand):
        # 哈希表记录手中各种颜色球的个数
        handH = dict(W=0, R=0, Y=0, B=0, G=0)
        for color in hand:
            handH[color] += 1
        return self.dfs(board, handH)

    def dfs(self, board, handH):
        n = len(board)
        if n == 0:
            return 0
        cnt = sys.maxint
        i = 0
        j = 0
        while i < n:
            while j < n and board[j] == board[i]:
                j += 1
            color = board[i]
            need = 3 - (j - i)
            # dfs
            if handH[color] >= need:
                nb = self.shrink(board[0:i] + board[j:])
                handH[color] -= need
                cur = self.dfs(nb, handH)
                if cur >= 0:
                    cnt = min(cnt, cur + need)
                handH[color] += need
            i = j
        return -1 if cnt == sys.maxint else cnt

    # 球碰撞消除
    @staticmethod
    def shrink(board):
        i = 0
        while i < len(board):
            j = i
            while j < len(board) and board[i] == board[j]:
                j += 1
            if j - i >= 3:
                board = board[0:i] + board[j:]
                i = 0
            else:
                i = j
        return board
"""

"""
Solution 2:
class Solution(object):
    def findMinStep(self, board, hand):
        def remove_sequences(board):    # recursively remove any sequences of length 3 or more
            start, end = 0, 0
            while end < len(board):
                if board[start] == board[end]:
                    end += 1
                elif end - start >= 3:
                    return remove_sequences(board[:start] + board[end:])
                else:
                    start = end
            if end - start >= 3:
                board = board[:start]
            return board

        def helper(board):
            if not board:
                return 0
            if not hand:
                return -1

            min_balls = 6           # since len(hand) <= 5
            start, end = 0, 0

            while end < len(board) + 1:

                if end == len(board) or board[start] != board[end]:
                    need = 3 - (end - start)    # number needed in hand to make a sequence of 3
                    colour = board[start]
                    if hand[colour] >= need:

                        hand[colour] -= need
                        next_board = remove_sequences(board[:start] + board[end:])
                        min_end = helper(next_board)
                        if min_end != -1:
                            min_balls = min(need + min_end, min_balls)
                        hand[colour] += need  # put balls back

                    start = end

                end += 1

            return -1 if min_balls == 6 else min_balls

        hand = Counter(hand)
        return helper(board)
"""

class Solution(object):
  def findMinStep(self, board, hand):
    """
    :type board: str
    :type hand: str
    :rtype: int
    """
    # change board to like [(a,3), (b,2), ...]
    board_ = []
    for i in range(len(board)):
      c = board[i]
      ind = ord(c) - ord('A')
      if len(board_) == 0 or board_[-1][0] != c:
        board_.append((c, 1))
      else:
        board_[-1] = (board_[-1][0], board_[-1][1]+1)

    # change hand to like [(a,2), (b,1), ...]
    hand_ = [0] * 26
    for i in range(len(hand)):
      c = hand[i]
      ind_ = ord(c) - ord('A')
      hand_[ind_] += 1
    # print board_, hand_

    res = helper(board_, hand_)
    return res

def helper(board_, hand_):
  # print 'working on', board_, hand_
  # prune
  i = 0
  while i < len(board_):
    # combine with previous
    if board_[i][1] >= 3:
      del board_[i]
    elif i > 0 and board_[i][0] == board_[i-1][0]:
      board_[i-1] = (board_[i-1][0], board_[i-1][1]+board_[i][1])
      del board_[i]
      if board_[i-1][1] >= 3:
        del board_[i-1]
        i -= 1
    else:
      i += 1
  # print 'after prune', board_
  if len(board_) == 0: return 0

  # for each item
  result = -1
  for i in range(len(board_)):
    # if can cancel
    c = board_[i][0] # char
    if board_[i][1] + hand_[ord(c)-ord('A')] >= 3: # cancellable
      new_board_ = [item for item in board_]
      new_hand_ = [item for item in hand_]
      # del new_board_[i]
      use = 3 - board_[i][1]
      new_hand_[ord(c)-ord('A')] = new_hand_[ord(c)-ord('A')] + board_[i][1] - 3
      new_board_[i] = (new_board_[i][0], 3)
      # print 'run sub',
      result_ = helper(new_board_, new_hand_)
      if result_ != -1: result_ += use 
      # print 'before', result_, result, 
      if result <0 or (result_ >= 0 and result_ < result):
        result = result_
      # print 'after', result_, result
  return result

if __name__ == "__main__":
  # print helper([('R', 1), ("B", 3), ("R",2),('B',1)], '')# "RBBBRRB", "")
  # print helper([('R', 1), ("R",2),('B',1)], )# "RBBBRRB", "")
  a = Solution()
  # print a.findMinStep("G", "GGGGG")
  # print a.findMinStep("B", "BB")
  print a.findMinStep("WRRBBW", "RB")
  print a.findMinStep("WWRRBBWW", "WRBRW")
  print a.findMinStep("G", "GGGGG")
  print a.findMinStep("RBYYBBRRB", "YRBGB")
