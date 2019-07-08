'''
438 Find All Anagrams in a String (Easy)

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

class Solution(object):
  def findAnagrams(self, s, p):
    # construct a set list
    p_set = {}
    for p_char in p:
      if p_set.has_key(p_char):
        p_set[p_char] += 1
      else:
        p_set[p_char] = 1
    # go through s
    p_len = len(p)
    s_len = len(s)
    s_set = {}
    s_set_cnt = 0
    result = []
    for i in range(s_len):
      # add s[i], s_set_cnt++
      if s_set.has_key(s[i]):
        s_set[s[i]] += 1
      else:
        s_set[s[i]] = 1
      s_set_cnt += 1
      # if s_set_cnt == p_len + 1, remove s[i-p_len()] from s_set
      if s_set_cnt == p_len + 1:
        tmp_c = s[i-p_len]
        s_set[tmp_c] -= 1
        s_set_cnt -= 1
        if s_set[tmp_c] == 0:
          s_set.pop(tmp_c)
      # if set equal, add i-p_len
      if s_set_cnt == p_len and s_set == p_set:
        result.append(i-p_len+1)
    return result


if __name__ == '__main__':
  a = Solution()
  print a.findAnagrams("cbaebabacd", 'abc')
