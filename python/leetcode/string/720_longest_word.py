"""
720. Longest Word in Dictionary (Easy)

Given a list of strings words representing an English Dictionary, find the longest word 
in words that can be built one character at a time by other words in words. If there 
is more than one possible answer, return the longest word with the smallest 
lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, 
"apple" is lexicographically smaller than "apply".

Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
"""

class Solution(object):
  def longestWord(self, words):
    longest = max([len(item) for item in words])
    maps = []
    for i in range(longest + 1):
      maps.append([])

    for item in words:
      len_ = len(item)
      maps[len_].append(item)
    print maps
    set_ = set()
    set_.add("")
    print "" in set_
    for len_ in range(1, longest+1):
      new_set = set()
      flag = False
      print len_,
      for word in maps[len_]:
        print word, word[:-1]
        if word[:-1] in set_:
          flag = True
          new_set.add(word)
      print set_, new_set, flag
      if flag:
        new_set, set_ = set(), new_set
      else:
        set_ = list(set_)
        set_.sort()
        return set_[0]
    # find smallest item in set_
    set_ = list(set_)
    set_.sort()
    return set_[0]


if __name__ == "__main__":
  a = Solution()
  print a.longestWord(['ww'])
  # print a.longestWord(["w","wo","wor","worl", "xxxxxxx"])
  arr = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
  print a.longestWord(arr)
