"""
927. Three Equal Parts (Hard)

Given an array A of 0s and 1s, divide the array into 3 non-empty parts such that all of these parts represent the same binary value.

If it is possible, return any [i, j] with i+1 < j, such that:

A[0], A[1], ..., A[i] is the first part;
A[i+1], A[i+2], ..., A[j-1] is the second part, and
A[j], A[j+1], ..., A[A.length - 1] is the third part.
All three parts have equal binary value.
If it is not possible, return [-1, -1].

Note that the entire part is used when considering what binary value it represents.  For example, [1,1,0] represents 6 in decimal, not 3.  Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.

 

Example 1:

Input: [1,0,1,0,1]
Output: [0,3]
Example 2:

Input: [1,1,0,1,1]
Output: [-1,-1]
 

Note:

3 <= A.length <= 30000
A[i] == 0 or A[i] == 1
"""

class Solution(object):
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        self.result = [-1, -1]

        def next_one(idx):
            # start from idx
            # return the idx of next one
            while idx < n and A[idx] == 0:
                idx += 1
            return idx

        start_idx = next_one(0)
        if start_idx == n:
            return [0, 2]

        # part 1: 0: len_
        l, r = start_idx, n - 2
        

        def check_valid(len_):
            # return -1, 0, 1 for len_ too short, ok, long
            # return 
            # part 1: 0..len_-1
            part1 = tuple(A[start_idx:len_])
            r_len = len_ - start_idx
            
            # part 2:
            idx2 = next_one(len_)
            part2 = tuple(A[idx2:idx2+r_len])
            if len(part2) < r_len:
                return 1, False

            # part 3:
            idx3 = next_one(idx2+r_len)
            part3 = tuple(A[idx3:])
            # print(len_, part1, part2, part3)
            if len(part3) < r_len:
                return 1, False
            elif len(part3) > r_len:
                return -1, False

            if part1 == part2 and part1 == part3:
                self.result = [len_-1, idx2+r_len]
                return 0, True
            else:
                return 0, False

        while l <= r:
            mid = (l+r) // 2

            res1, res2 = check_valid(mid)
            if res1 > 0:
                r = mid -1 
            elif res1 < 0:
                l = mid + 1
            else:
                return self.result
        return self.result


if __name__ == "__main__":
    a = Solution()
    print(a.threeEqualParts([1,0,1,0,1]))
    print(a.threeEqualParts([1,1,0,1,1]))
