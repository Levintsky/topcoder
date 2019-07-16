"""
1138. Alphabet Board Path (Medium)

On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"].

We may make the following moves:

'U' moves our position up one row, if the square exists;
'D' moves our position down one row, if the square exists;
'L' moves our position left one column, if the square exists;
'R' moves our position right one column, if the square exists;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.

Example 1:

Input: target = "leet"
Output: "DDR!UURRR!!DDD!"
Example 2:

Input: target = "code"
Output: "RR!DDRR!UUL!R!"

Constraints:

1 <= target.length <= 100
target consists only of English lowercase letters.
"""

class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        memo_pos = {}
        for i in range(26):
            c = chr(ord('a') + i)
            rr, cc = i // 5, i % 5
            memo_pos[c] = (rr, cc)
        if target == "":
            return ""

        n = len(target)
        target = 'a' + target
        res = []

        def gen(n1, n2, cc1, cc2):
            tmpres = ''
            if n1 > n2:
                tmpres = (n1 - n2) * cc1
            else:
                tmpres = (n2 - n1) * cc2
            return tmpres

        for i in range(n):
            c1, c2 = target[i], target[i+1]
            rr1, cc1 = memo_pos[c1]
            rr2, cc2 = memo_pos[c2]
            if c1 == 'z':
                res.append(gen(rr1, rr2, 'U', 'D'))
                res.append(gen(cc1, cc2, 'L', 'R'))
            else:
                res.append(gen(cc1, cc2, 'L', 'R'))
                res.append(gen(rr1, rr2, 'U', 'D'))

            res.append('!')
        return "".join(res)


if __name__ == "__main__":
    a = Solution()
    print(a.alphabetBoardPath("leet"))
    print(a.alphabetBoardPath("code"))
    print(a.alphabetBoardPath("zb"))
    print(a.alphabetBoardPath("bz"))

