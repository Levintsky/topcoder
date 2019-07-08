'''
3. Longest Substring Without Repeating Characters (Medium)

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer 
must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
  def lengthOfLongest(self, s):
    if len(s) <= 1:
      return len(s)
    st = 0
    i = 1
    # st..i 
    best = 0
    rec = set([s[0]])
    while(i<len(s)):
      if s[i] in rec:
        # move st until no duplicate
        while(s[st]!=s[i]):
          rec.remove(s[st])
          st += 1
        st += 1
      else:
        rec.add(s[i])
      print i, rec, s[st:i+1]
      best = max(best, i-st+1)
      i += 1
    return best


if __name__ == '__main__':
  a = Solution()
  print a.lengthOfLongest('abcabcbb')
  print a.lengthOfLongest('bbbbb')
  print a.lengthOfLongest('pwwkew')
