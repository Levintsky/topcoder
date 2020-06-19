class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        slots1 = [tuple(item) for item in slots1]
        slots2 = [tuple(item) for item in slots2]
        slots1.sort()
        slots2.sort()
        
        i1, i2 = 0, 0
        n1, n2 = len(slots1), len(slots2)
        while i1 < n1 and i2 < n2:
            # no overlap cases
            if slots1[i1][1] <= slots2[i2][0]:
                i1 += 1
            elif slots2[i2][1] <= slots1[i1][0]:
                i2 += 1
            else:
                start = max(slots1[i1][0], slots2[i2][0])
                end = min(slots1[i1][1], slots2[i2][1])
                if end - start >= duration:
                    return [start, start+duration]
                if slots1[i1][1] <= slots2[i2][1]:
                    i1 += 1
                else:
                    i2 += 1
        return []


if __name__ == "__main__":
    a = Solution()
    print(a.minAvailableDuration(slots1, slots2, duration))
