'''
557. Reverse Words in a String III (Easy)

Given a string, you need to reverse the order of characters in each word within a 
sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any 
extra space in the string.
'''

class Solution(object):
  def reverseWords(self, s):
    n = len(s)
    if n <= 1: return s
    s_list = s.split(' ')
    new_s = ''
    for item in s_list:
      new_s += item[::-1]
      new_s += ' '
    new_s = new_s[:-1]
    return new_s

  def solution2(self, s):
    s_list = s.split(' ')
    s_list = [item[::-1] for item in s_list]
        
    return ' '.join(s_list)


if __name__ == '__main__':
  a = Solution()
  print a.reverseWords("Let's take LeetCode contest")
