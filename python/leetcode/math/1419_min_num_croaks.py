"""
1419. Minimum Number of Frogs Croaking (Medium)

Given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple “croak” are mixed. Return the minimum number of different frogs to finish all the croak in the given string.

A valid "croak" means a frog is printing 5 letters ‘c’, ’r’, ’o’, ’a’, ’k’ sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of valid "croak" return -1.

Example 1:

Input: croakOfFrogs = "croakcroak"
Output: 1 
Explanation: One frog yelling "croak" twice.
Example 2:

Input: croakOfFrogs = "crcoakroak"
Output: 2 
Explanation: The minimum number of frogs is two. 
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".
Example 3:

Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.
Example 4:

Input: croakOfFrogs = "croakcroa"
Output: -1
 

Constraints:

1 <= croakOfFrogs.length <= 10^5
All characters in the string are: 'c', 'r', 'o', 'a' or 'k'.
"""

import collections
import heapq

class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        if len(croakOfFrogs) % 5 != 0:
            return -1
        if len(croakOfFrogs) == 0:
            return 0

        memo = ['c', 'r', 'o', 'a', 'k']
        remain = ""
        id_ = 0
        for c in croakOfFrogs:
            if c == memo[id_]:
                id_ = (id_ + 1) % 5
            else:
                remain += c
        res = self.minNumberOfFrogs(remain)
        if res != -1:
            return res + 1
        else:
            return -1

    def solve2(self, croakOfFrogs):
        q = []
        memo = {'c':0, 'r':1, 'o':2, 'a':3, 'k':4}
        for i in range(5):
            q.append(collections.deque())
        valid_set = set()
        if len(croakOfFrogs) % 5 != 0:
            return -1

        res = []
        for i, c in enumerate(croakOfFrogs):
            idx = memo[c]
            q[idx].append(i)
            # check unvalid
            if idx > 0 and len(q[idx]) > len(q[idx-1]):
                return -1
            # check remove
            len_ = [len(q[ii]) for ii in range(5)]
            if min(len_) > 0:
                h, t = q[0][0], q[-1][0]
                for ii in range(5):
                    q[ii].popleft()
                if len(res) == 0 or h < res[0]:
                    heapq.heappush(res, t)
                else:
                    _ = heapq.heappop(res)
                    heapq.heappush(res, t)
        len_ = [len(q[ii]) for ii in range(5)]
        if max(len_) == 0:
            return len(res)
        else:
            return -1

"""
Super smart solution:

Increase number of frogs singing this letter, and decrease number singing previous letter.
When a frog sings 'c', we increase the total number of frogs.
When a frog sings 'k', we decrease the total number of frogs.
If some frog is singing a letter, but no frog sang the previous letter, we return -1.

int minNumberOfFrogs(string croakOfFrogs) {
    int cnt[5] = {}, frogs = 0, max_frogs = 0;
    for (auto ch : croakOfFrogs) {
        auto n = string("croak").find(ch);
        ++cnt[n];
        if (n == 0)
            max_frogs = max(max_frogs, ++frogs);
        else if (--cnt[n - 1] < 0)
            return -1;
        else if (n == 4)
            --frogs;
    }
    return frogs == 0 ? max_frogs : -1;
}
"""


if __name__ == "__main__":
    a = Solution()
    """
    print(a.minNumberOfFrogs("croakcroak"))
    print(a.minNumberOfFrogs("crcoakroak"))
    print(a.minNumberOfFrogs("croakcrook"))
    print(a.minNumberOfFrogs("croakcroa"))
    """
    print(a.solve2("croakcroak"))
    print(a.solve2("crcoakroak"))
    print(a.solve2("croakcrook"))
    print(a.solve2("croakcroa"))