"""
186. Reverse Words in a String II (Medium)

Given an input string, reverse the string word by word. A word is defined as a 
sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always 
separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?
"""

class Solution:
    def reverseWords(self, s):
        s_list = s.split(' ')
        s_list = s_list[::-1]
        result = ' '.join(s_list)
        return result


if __name__ == "__main__":
  a = Solution()
  print a.reverseWords("the sky is blue")
