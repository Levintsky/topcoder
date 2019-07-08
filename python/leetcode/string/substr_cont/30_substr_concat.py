'''
30. Substring with Concatenation of All Words (Hard)

You are given a string, s, and a list of words, words, that are all of the same length. 
Find all starting indices of substring(s) in s that is a concatenation of each word in 
words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''

"""
key-point:
after check
j: j + wl * n
next time just minus j:j+wl, and add the latest
save computation!!!
"""

class Solution(object):
  def findSubstring(self, s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    wl = len(words[0])
    n = len(s)
    stat = {}
    for word in words:
      stat[word] = stat.get(word, 0) + 1

    result = []
    for i in range(wl):
      cnt = 0
      j = i
      curr_stat = {}
      begin = j
      while j <= n - wl:
        sub = s[j:j+wl]
        print j, sub
        if sub in stat:
          curr_stat[sub] = curr_stat.get(sub, 0) + 1
          if curr_stat[sub] <= stat[sub]:
            # within range, accumulate state
            cnt += 1
          else:
            # sub appears more than once
            start = j - wl * cnt
      
            sub_ = s[start:start+wl]
            while sub_ != sub:
              curr_stat[sub_] -= 1
              cnt -= 1
              start += wl
              sub_ = s[start:start+wl]
          if cnt == len(words):
            result.append(j-(len(words)-1)*wl)
        else:
          curr_stat = {}
          cnt = 0 
        j += wl

    return result


if __name__ == "__main__":
  a = Solution()
  # print a.findSubstring("barfoothefoobarman", ["foo", "bar"])
  print a.findSubstring("barfoobar", ["foo", "bar"])
