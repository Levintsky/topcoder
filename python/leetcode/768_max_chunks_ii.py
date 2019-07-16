class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        res = self.helper(arr, 0, n-1)
        return res
        
    def helper(self, arr, i, j):
        # return the result of i - j
        if i > j:
            return 0
        if i == j:
            return 1
        # find min, find max
        min_index = j # rightmost min-index
        for jj in range(j, i-1, -1):
            if arr[jj] < arr[min_index]:
                min_index = jj
        # leftmost max-index
        max_index = i
        for ii in range(i, j+1):
            if arr[ii] > arr[max_index]:
                max_index = ii
        # special case 1: min == max
        if arr[min_index] == arr[max_index]:
            return j-i+1
        # special case 2: min_index > max_index
        if min_index > max_index:
            return 1
        res = 0
        for ii in range(i, j+1):
            if arr[ii] == arr[min_index]:
                res += 1
            else:
                break
        for jj in range(j, i-1, -1):
            if arr[jj] == arr[max_index]:
                res += 1
            else:
                break
        return res + 1 + self.helper(arr, min_index+1, max_index-1)


if __name__ == "__main__":
    a = Solution()
    print(a.maxChunksToSorted([2,3,1,4,4]))