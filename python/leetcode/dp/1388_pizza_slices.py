"""
1388. Pizza With 3n Slices (Hard)

There is a pizza with 3n slices of varying size, you and your friends will take slices of pizza as follows:

You will pick any pizza slice.
Your friend Alice will pick next slice in anti clockwise direction of your pick. 
Your friend Bob will pick next slice in clockwise direction of your pick.
Repeat until there are no more slices of pizzas.
Sizes of Pizza slices is represented by circular array slices in clockwise direction.

Return the maximum possible sum of slice sizes which you can have.

Example 1:

Input: slices = [1,2,3,4,5,6]
Output: 10
Explanation: Pick pizza slice of size 4, Alice and Bob will pick slices with size 3 and 5 respectively. Then Pick slices with size 6, finally Alice and Bob will pick slice of size 2 and 1 respectively. Total = 4 + 6.

Example 2:

Input: slices = [8,9,8,6,1,1]
Output: 16
Output: Pick pizza slice of size 8 in each turn. If you pick slice with size 9 your partners will pick slices of size 8.

Example 3:

Input: slices = [4,1,2,5,8,3,1,9,7]
Output: 21

Example 4:

Input: slices = [3,1,2]
Output: 3

Constraints:

1 <= slices.length <= 500
slices.length % 3 == 0
1 <= slices[i] <= 1000
"""

"""
Don't overthink!
Someone happened to ask me this problem ealier.
I told him to do this 213. House Robber II
Almost the same.

The interruption of this question is:
get n elements from an an array of sizes 3*n.
None of the selected n elements could be neighbor to each others.
And because its in cycle,
A[0] and A[n-1] cannot be chosen together.
After understanding this, the question become much easier.

dfs can be compressed to one line but too long.


Python:

    def maxSizeSlices(self, A):
        @functools.lru_cache(None)
        def dp(i, j, k, cycle=0):
            if k == 1: return max(A[i:j + 1])
            if j - i + 1 < k * 2 - 1: return -float('inf')
            return max(dp(i + cycle, j - 2, k - 1) + A[j], dp(i, j - 1, k))
        return dp(0, len(A) - 1, len(A) // 3, 1)

class Solution:
    def maxSizeSlices(self, A):
        @functools.lru_cache(None)
        def dp(i, j, k, cycle=0):
            # i,j = start,end (inclusive)
            # k = remaining
            # cycle (see comment on cycle variable)
            
            if k == 1:
                # one remaining, calculate immediately
                return max(A[i:j + 1])
            
            if j - i + 1 < k * 2 - 1: 
                # not possible because not enough elements remain
                return -float('inf')
            
            return max(A[j] +                 # take last element
                       dp(i + cycle, j - 2,   # dp on i to j-2
                          k - 1),             # one less element left to take
                          # (on the cycle variable)
                          # if the last element of the inital array is taken
                          # you cannot take the first element of the inital array
                       # Alternatively, you choose not to take element j
                       dp(i, j - 1,    # dp on i to j-1
                          k))          # same number of elements to take

        return dp(0, len(A) - 1, # dp on 0 to length-1
                  len(A) // 3,   # number of elements to take
                  1)             # see comment on cycle variable
            
        # lru_cache to reduce search space
"""

class Solution(object):
    def maxSizeSlices(self, slices):
        """
        :type slices: List[int]
        :rtype: int
        """
        self.memo = {}
        n = len(slices)

        if n == 3:
            return max(slices)

        def mem_dp(i, j): # no warp
            # best result of [i..j]
            if i == 3 and j == 8:
                pass

            if (i, j) in self.memo: # corner case 0: done
                return self.memo[(i, j)]
            elif (i + 1) % n == j: # corner case 1: empty
                return 0
            elif (i + 2) % n == j: # 3 items
                self.memo[(i, j)] = slices[(i + 1) % n]
                return self.memo[(i,j)]
            # non-trivial cases
            if j > i:
                len_ = j - i + 1
            else:
                len_ = j + n + 1 - i
            id_ = (i+1) % n
            curr = -100000
            # case 1: id_ in middle
            for _ in range(len_ // 3):
                # [i+1, id_-1]
                if id_ == (i+1)%n:
                    res1 = 0
                else:
                    res1 = mem_dp((i+1)%n, (id_-1)%n)
                # [id_+1, j-1]
                if (id_+1) % n == j:
                    res2 = 0
                else:
                    res2 = mem_dp((id_+1)%n, (j-1)%n)
                curr = max(curr, res1 + res2 + slices[id_])
                id_ = (id_+3)%n
            # case 2: separate
            id_ = (i + 2) % n
            for _ in range(len_ // 3):
                res1 = mem_dp(i, id_)
                res2 = mem_dp((id_+1)%n, j)
                curr = max(curr, res1 + res2)
                id_ = (id_+3)%n

            self.memo[(i, j)] = curr
            return curr

        res = -100000
        for id1 in range(n):
            for id2 in range(id1+1, n, 3):
                for id3 in range(id2+1, n, 3):
                    if id1 + 1 == id2:
                        res1 = 0
                    else:
                        res1 = mem_dp(id1+1, id2-1)
                    if id2 + 1 == id3:
                        res2 = 0
                    else:
                        res2 = mem_dp(id2+1, id3-1)
                    if id1 == 0 and id3 == n-1:
                        res3 = 0
                    else:
                        res3 = mem_dp((id3+1)%n, (id1-1)%n)
                    pick = max(slices[id1], slices[id2], slices[id3])
                    res = max(res, pick+res1+res2+res3)
        print(self.memo)
        return res


if __name__ == "__main__":
    a = Solution()
    # print(a.maxSizeSlices([1,2,3,4,5,6]))
    # print(a.maxSizeSlices([8,9,8,6,1,1]))
    # print(a.maxSizeSlices([4,1,2,5,8,3,1,9,7]))
    # print(a.maxSizeSlices([3,1,2]))
    print(a.maxSizeSlices([10,9,1,10,8,5,10,2,2]))
