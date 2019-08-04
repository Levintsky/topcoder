"""
846. Hand of Straights (Medium)

Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.

Note:

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length
"""

class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        n = len(hand)
        if n % W != 0:
            return False
        hand.sort()
        s = [] # stack to keep minimum
        memo = {}
        for item in hand:
            if not s or item > s[-1]:
                s.append(item)
            memo[item] = memo.get(item, 0) + 1
        s = s[::-1]
        # print(s)
        while len(s) > 0:
            while s and s[-1] not in memo:
                _ = s.pop()
            if not s:
                return True

            # item -> item + W - 1
            for i in range(s[-1], s[-1] + W):
                if i not in memo:
                    return False
                memo[i] -= 1
                if memo[i] == 0:
                    del memo[i]
        return True

    # smarter
    def isNStraightHand(self, hand, W):
        c = collections.Counter(hand)
        for i in sorted(c):
            if c[i] > 0:
                for j in range(W)[::-1]:
                    c[i + j] -= c[i]
                    if c[i + j] < 0:
                        return False
        return True

if __name__ == "__main__":
    a = Solution()
    print(a.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
    print(a.isNStraightHand([1,2,3,6,2,3,4,7,8], 1))
    print(a.isNStraightHand([1,2,3,4,5], 4))
    print(a.isNStraightHand([1,1,2,2,3,3], 3))
