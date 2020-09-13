"""
1562. Find Latest Group of Size M (Medium)

Given an array arr that represents a permutation of numbers from 1 to n. You have a binary string of size n that initially has all its bits set to zero.

At each step i (assuming both the binary string and arr are 1-indexed) from 1 to n, the bit at position arr[i] is set to 1. You are given an integer m and you need to find the latest step at which there exists a group of ones of length m. A group of ones is a contiguous substring of 1s such that it cannot be extended in either direction.

Return the latest step at which there exists a group of ones of length exactly m. If no such group exists, return -1.

 

Example 1:

Input: arr = [3,5,1,2,4], m = 1
Output: 4
Explanation:
Step 1: "00100", groups: ["1"]
Step 2: "00101", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "11101", groups: ["111", "1"]
Step 5: "11111", groups: ["11111"]
The latest step at which there exists a group of size 1 is step 4.
Example 2:

Input: arr = [3,1,5,4,2], m = 2
Output: -1
Explanation:
Step 1: "00100", groups: ["1"]
Step 2: "10100", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "10111", groups: ["1", "111"]
Step 5: "11111", groups: ["11111"]
No group of size 2 exists during any step.
Example 3:

Input: arr = [1], m = 1
Output: 1
Example 4:

Input: arr = [2,1], m = 2
Output: 2
 

Constraints:

n == arr.length
1 <= n <= 10^5
1 <= arr[i] <= n
All integers in arr are distinct.
1 <= m <= arr.length
"""

class Solution(object):
    def solve(self, arr, m):
        memo_l2r = {}
        memo_r2l = {}
        best = -1
        curr = 0
        for i, item in enumerate(arr):
            to_remove = []
            real_l, real_r = item, item
            if item - 1 in memo_r2l:
                to_remove.append([memo_r2l[item-1], item-1])
                real_l = memo_r2l[item-1]
            if item + 1 in memo_l2r:
                to_remove.append([item+1, memo_l2r[item+1]])
                real_r = memo_l2r[item+1]
            for l, r in to_remove:
                if r - l + 1 == m:
                    curr -= 1
                del memo_l2r[l]
                del memo_r2l[r]
            memo_l2r[real_l] = real_r
            memo_r2l[real_r] = real_l
            if real_r - real_l + 1 == m:
                curr += 1
            if curr > 0:
                best = i + 1
        return best

    def findLatestStep(self, A, m):
        length = [0] * (len(A) + 2)
        count = [0] * (len(A) + 1)
        res = -1
        for i, a in enumerate(A):
            left, right = length[a - 1], length[a + 1]
            length[a] = length[a - left] = length[a + right] = left + right + 1
            count[left] -= 1
            count[right] -= 1
            count[length[a]] += 1
            if count[m]:
                res = i + 1
        return res


if __name__ == "__main__":
    a = Solution()
    # print(a.findLatestStep([3,5,1,2,4], 1))
    print(a.solve([3,5,1,2,4], 1))
    print(a.solve([3,1,5,4,2], 2))
    print(a.solve([1], 1))
    print(a.solve([2, 1], 2))
    print(a.solve([1, 2], 1))
