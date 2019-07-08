"""
246. Strobogrammatic Number (Easy)

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
"""

class Solution(object):
  def isStrobogrammatic(self, num):
    """
    :type num: str
    :rtype: bool
    """
    i, j = 0, len(num) - 1
    while i <= j:
      print(i, j, num[i], num[j])
      if num[i] == "6" and num[j] == "9":
        i, j = i + 1, j - 1
      elif num[i] == "9" and num[j] == "6":
        i, j = i + 1, j - 1
      elif num[i] == "8" and num[j] == "8":
        i, j = i + 1, j - 1
      elif num[i] == "1" and num[j] == "1":
        i, j = i + 1, j - 1
      elif num[i] == "0" and num[j] == "0":
        i, j = i + 1, j - 1
      else:
        print(False, num[i], num[j])
        return False
    return True


if __name__ == "__main__":
  a = Solution()
  print a.isStrobogrammatic("9680186699810896")
