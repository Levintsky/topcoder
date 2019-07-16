"""
1099. Two Sum Less Than K (Easy)

Given an array A of integers and integer K, return the maximum S such that 
there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying 
this equation, return -1.

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation: 
In this case it's not possible to get a pair sum less that 15.

Note:

1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000
"""

import bisect

class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        if n < 2: return -1
        best = A[0] + A[1]
        res = []
        for i, item in enumerate(A):
            if len(res) == 0:
                res.append(item)
            else:
                idx = bisect.bisect_left(res, K-1-item)
                if idx < len(res) and res[idx] == K-1-item:
                    return K-1
                idx = max(idx-1, 0)
                if idx < len(res) and res[idx] + item < K:
                    if best >= K: best = res[idx] + item
                    else: best = max(best, res[idx] + item)
            if item < K:
                bisect.insort(res, item)
        if best >= K:
            return -1
        else:
            return best


if __name__ == "__main__":
    a = Solution()
    print(a.twoSumLessThanK([34,23,1,24,75,33,54,8], 60))
    print(a.twoSumLessThanK([10,20,30], 15))
    arr = [254,914,110,900,147,441,209,122,571,942,136,350,160,127,178,839,201,386,462,45,735,467,153,415,875,282,204,534,639,994,284,320,865,468,1,838,275,370,295,574,309,268,415,385,786,62,359,78,854,944]
    # arr = [499,451,631,986,937,847,540,697,502,12,166,633,536,603,316,645,182,976,79,404,893,749,823,753,428,943,868,755,223,904,205,541,407,308,829,751,703,156,529,67,785,422,691,905,928,706,594,203,548,662]   
    print(a.twoSumLessThanK(arr, 200))

"""
[Java] Sort then push from two ends.

Note: 1) I have no premium subscription and can NO longer read comments under locked problems, though I can still edit my post now. 2) Sorry that I can NOT answer your questions.
Sort the input A;
Push from the two ends and attempt to find any addition of the two elements < K; if the addition >= K, then decrease the high bound and hence tentatively get a smaller addition; otherwise, increase low bound to find a bigger addition;
repeat 2 till the end.
    public int twoSumLessThanK(int[] A, int K) {
        Arrays.sort(A); // Time cost O(nlogn).
        int max = -1, i = 0, j = A.length - 1; 
        while (i < j) {
            int sum = A[i] + A[j];
            if (sum < K) { // find one candidate.
                max = Math.max(max, sum);
                ++i; // increase the smaller element.
            }else { // >= sum.
                --j; // decrease the bigger element.
            }
        }
        return max;
    }
"""