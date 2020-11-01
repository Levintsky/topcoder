class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        n = len(s)
        nums = []
        for c in s:
            nums.append(ord(c) - ord('0'))
        
        # enumerate rotate
        memo = set()
        best = s
        idx = 0
        for i in range(n):
            idx = (i * b) % n
            if idx in memo:
                break
            # change odd only to get min
            besto = nums[1]
            for offset in range(10):
                besto = min(besto, (nums[1] + offset * a) % 10)
            offset = besto - nums[1]
            for j in range(n):
                if j % 2 == 1:
                    nums[j] = (nums[j] + offset) % 10
            print(nums)
            nums_ = [str(i) for i in nums]
            tmp = "".join(nums_)
            best = min(best, tmp)
            print(i, tmp, best)
            memo.add(idx)
            nums = nums[b:] + nums[:b]

        return best
            

if __name__ == "__main__":
    a = Solution()
    print(a.findLexSmallestString("43987654", 7, 3))