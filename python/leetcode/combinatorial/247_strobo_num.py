"""
247. Strobogrammatic Number II (Medium)

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].

"""

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = self.helper(n)
        if n == 1:
            return ret
        ret = [item for item in ret if item[0] != "0"]
        return ret
       

    def helper(self, n):
        if n == 2:
            return ["00", "11","69","88","96"]
        if n == 1:
            return ["0", "1", "8"]

        ret = self.helper(n - 2)
        newret = []
        for item in ret:
            newret.append("1" + item + "1")
            newret.append("6" + item + "9")
            newret.append("9" + item + "6")
            newret.append("8" + item + "8")
            newret.append("0" + item + "0")
        return newret

if __name__ == "__main__":
  a = Solution()
  print(a.findStrobogrammatic(4))
