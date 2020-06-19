"""
777. Swap Adjacent in LR String (Medium)

In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

Example:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
 

Constraints:

1 <= len(start) == len(end) <= 10000.
Both start and end will only consist of characters in {'L', 'R', 'X'}.
"""

class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        def transform(s):
            l = []
            for i, c in enumerate(s):
                if c == 'X':
                    continue
                else:
                    l.append((c, i))
            return l
        
        sl = transform(start)
        el = transform(end)
        print(sl, el)
        if len(sl) != len(el):
            return False
        
        for item1, item2 in zip(sl, el):
            if item1[0] == item2[0]:
                if item1[0] == 'L' and item1[1] >= item2[1]:
                    continue
                if item1[0] == 'R' and item1[1] <= item2[1]:
                    continue
            return False
        return True


if __name__ == "__main__":
    a = Solution()
    print(a.canTransform("RXXLRXRXL", "XRLXXRRLX"))
    print(a.canTransform("XXXXXLXXXX", "LXXXXXXXXX"))
    print(a.canTransform("XXXXXLXXXLXXXX", "XXLXXXXXXXXLXX"))
    print(a.canTransform("XXXXXLXXXX", "LXXXXXXXXX"))
