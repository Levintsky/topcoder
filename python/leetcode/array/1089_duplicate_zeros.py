"""
1089. Duplicate Zeros (Easy)

Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]

Note:

1 <= arr.length <= 10000
0 <= arr[i] <= 9
"""


class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        arr2 = [item for item in arr]
        n = len(arr)
        i, j = 0, 0
        while j < n:
            if arr[i] != 0:
                arr2[j] = arr[i]
            else:
                arr2[j] = 0
                j += 1
                if j < n:
                    arr2[j] = 0
            i += 1
            j += 1
        for i in range(n):
            arr[i] = arr2[i]
        print(arr)
        return

    def solve2(self, arr):
        n = len(arr)
        shift = 0
        i = 0
        while i + shift < n - 1:
            if arr[i] == 0:
                shift += 1
            i += 1
        j = n - 1
        if arr[i] == 0:
            if i + shift > n - 1:
                i -= 1
            else:
                # shift += 1
                i -= 1
                arr[-1] = 0
                j -= 1
        while j >= 0:
            if arr[j - shift] != 0:
                # print(j, j-shift)
                arr[j] = arr[j - shift]
            else:
                # print(j, j-1)
                arr[j] = 0
                j -= 1
                arr[j] = 0
                shift -= 1
            j -= 1
        return


if __name__ == "__main__":
    a = Solution()
    # print(a.duplicateZeros([1,0,2,3,0,4,5,0]))
    print(a.solve2([1, 0, 2, 3, 0, 4, 5, 0]))
    # print(a.duplicateZeros([1,2,3]))
    print(a.solve2([1, 2, 3]))
    print(a.solve2([8, 4, 5, 0, 0, 0, 0, 7]))
    # array = [9,0,9,0,6,0,0,0,1,1,6,5,4,4,8,3,0,0,0,1,5,3,0,0,7,2,1,0,2,0,9,1,0,2,0,0,0,0,0,0,0,6,0,0,7,9,0,8,7,0,9,7,1,0,2,0,0,0,0,9,0,0,0,0]
    # print(a.solve2(array))
    print(a.solve2([1, 5, 2, 0, 6, 8, 0, 6, 0]))
