"""
862. Shortest Subarray with Sum at Least K (Hard)

Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

 

Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3
 

Note:

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9
"""

"""
Solution: O(N) with deque()

Calculate prefix sum B of list A.
B[j] - B[i] represents the sum of subarray A[i] ~ A[j-1]
Deque d will keep indexes of increasing B[i].
For every B[i], we will compare B[i] - B[d[0]] with K.

Time Complexity:
Loop on B O(N)
Every index will be pushed only once into deque. O(N)

C++:

    int shortestSubarray(vector<int> A, int K) {
        int N = A.size(), res = N + 1;
        vector<int> B(N + 1, 0);
        for (int i = 0; i < N; i++) B[i + 1] = B[i] + A[i];
        deque<int> d;
        for (int i = 0; i < N + 1; i++) {
            while (d.size() > 0 && B[i] - B[d.front()] >= K)
                res = min(res, i - d.front()), d.pop_front();
            while (d.size() > 0 && B[i] <= B[d.back()]) d.pop_back();
            d.push_back(i);
        }
        return res <= N ? res : -1;
    }
Java:

    public int shortestSubarray(int[] A, int K) {
        int N = A.length, res = N + 1;
        int[] B = new int[N + 1];
        for (int i = 0; i < N; i++) B[i + 1] = B[i] + A[i];
        Deque<Integer> d = new ArrayDeque<>();
        for (int i = 0; i < N + 1; i++) {
            while (d.size() > 0 && B[i] - B[d.getFirst()] >=  K)
                res = Math.min(res, i - d.pollFirst());
            while (d.size() > 0 && B[i] <= B[d.getLast()]) d.pollLast();
            d.addLast(i);
        }
        return res <= N ? res : -1;
    }
Python:

    def shortestSubarray(self, A, K):
        N = len(A)
        B = [0] * (N + 1)
        for i in range(N): B[i + 1] = B[i] + A[i]
        d = collections.deque()
        res = N + 1
        for i in xrange(N + 1):
            while d and B[i] - B[d[0]] >= K: res = min(res, i - d.popleft())
            while d and B[i] <= B[d[-1]]: d.pop()
            d.append(i)
        return res if res <= N else -1

FAQ
Q: How to think of such solutions?
A: Basic idea, for array starting at every A[i], find the shortest one with sum at leat K.
In my solution, for B[i], find the smallest j that B[j] - B[i] >= K.
Keep this in mind for understanding two while loops.

Q: What is the purpose of first while loop?
A: For the current prefix sum B[i], it covers all subarray ending at A[i-1].
We want know if there is a subarray, which starts from an index, ends at A[i-1] and has at least sum K.
So we start to compare B[i] with the smallest prefix sum in our deque, which is B[D[0]], hoping that [i] - B[d[0]] >= K.
So if B[i] - B[d[0]] >= K, we can update our result res = min(res, i - d.popleft()).
The while loop helps compare one by one, until this condition isn't valid anymore.

Q: Why we pop left in the first while loop?
A: This the most tricky part that improve my solution to get only O(N).
D[0] exists in our deque, it means that before B[i], we didn't find a subarray whose sum at least K.
B[i] is the first prefix sum that valid this condition.
In other words, A[D[0]] ~ A[i-1] is the shortest subarray starting at A[D[0]] with sum at least K.
We have already find it for A[D[0]] and it can't be shorter, so we can drop it from our deque.

Q: What is the purpose of second while loop?
A: To keep B[D[i]] increasing in the deque.

Q: Why keep the deque increase?
A: If B[i] <= B[d.back()] and moreover we already know that i > d.back(), it means that compared with d.back(),
B[i] can help us make the subarray length shorter and sum bigger. So no need to keep d.back() in our deque.


Please let me know if there is still anything unclear.
"""

import collections


class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        N = len(A)
        B = [0] * (N + 1)
        for i in range(N):
            B[i + 1] = B[i] + A[i]
        # an increasing value
        d = collections.deque()
        res = N + 1
        for i in range(N + 1):
            # first while-loop: if A[i] is large and there is a subarray >= K
            # then update result, popleft
            while d and B[i] - B[d[0]] >= K:
                res = min(res, i - d.popleft())
            # in case of a negative, popright to keep d increaing
            while d and B[i] <= B[d[-1]]:
                d.pop()
            d.append(i)
        return res if res <= N else -1

    def solve2(self, A, K):
        n = len(A)
        B = [0] * (n + 1)
        for i in range(n):
            B[i + 1] = B[i] + A[i]
        res = n + 1
        d = collections.deque()
        # find min(j-i), s.t. i < j and B[j]-B[i] >= K
        for i in range(n + 1):
            # there is a subarray satisfying
            while d and B[i] - B[d[0]] >= K:
                res = min(res, i - d.popleft())
            while d and B[i] <= B[d[-1]]:
                d.pop()
            d.append(i)
        if res > n:
            return -1
        else:
            return res


if __name__ == "__main__":
    a = Solution()
    # print(a.shortestSubarray([2,-1,2], 3))
    print(a.solve2([2, -1, 2], 3))
