"""
1035. Uncrossed Lines (Medium)

We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw a straight line connecting two numbers A[i] and B[j] as long as A[i] == B[j], and the line we draw does not intersect any other connecting (non-horizontal) line.

Return the maximum number of connecting lines we can draw in this way.

Example 1:

Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.

Example 2:

Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3

Example 3:

Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2

Note:

1 <= A.length <= 500
1 <= B.length <= 500
1 <= A[i], B[i] <= 2000
"""


class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        B_dict = {}
        for idx, item in enumerate(B):
            if item not in B_dict:
                B_dict[item] = [idx]
            else:
                B_dict[item].append(idx)
        # print(B_dict)
        curr = [0]
        for idx, item in enumerate(A):
            new_curr = [0]
            # print(item, ":")
            for len_ in range(len(curr)):
                # new_curr.append(curr[len_])
                if item in B_dict:
                    curr_end = curr[len_] - 1
                    # print("here", curr_end)
                    # find first index in B[item] s.t.
                    flag = False
                    for idx in B_dict[item]:
                        if idx > curr_end:
                            new_curr.append(idx + 1)
                            flag = True
                            break
                    if not flag:  # if found
                        if len_ != len(curr) - 1:
                            new_curr.append(curr[len_ + 1])
                    else:
                        if len_ != len(curr) - 1:
                            new_curr[-1] = min(new_curr[-1], curr[len_ + 1])
                elif len_ != len(curr) - 1:
                    new_curr.append(curr[len_ + 1])
            # print(curr, new_curr)
            curr = new_curr
        return len(curr) - 1


if __name__ == "__main__":
    a = Solution()
    print(a.maxUncrossedLines([1, 4, 2], [1, 2, 4]))
    print(a.maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]))
    print(a.maxUncrossedLines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]))
