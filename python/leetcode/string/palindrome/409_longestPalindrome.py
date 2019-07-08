'''
409 Longest Palindrome (Easy)

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''

class Solution(object):
  def longestPalindrome(self, s):
    if not s:
      return 0
    count_dict = {}
    for i in range(len(s)):
      if count_dict.has_key(s[i]):
        count_dict[s[i]] += 1
      else:
        count_dict[s[i]] = 1
    odd_flag = False
    cnt = 0
    for _, v in count_dict.items():
      if v % 2 == 1:
        odd_flag = True
        cnt += v-1
      else:
        cnt += v
    if odd_flag:
      cnt += 1
    return cnt


if __name__ == '__main__':
  a = Solution()
  print a.longestPalindrome('abccccdd')
