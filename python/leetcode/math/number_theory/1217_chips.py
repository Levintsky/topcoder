class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        odd, even = 0, 0
        for item in chips:
            if item % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(even, odd)
