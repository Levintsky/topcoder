"""
288. Unique Word Abbreviation (Medium)

An abbreviation of a word follows the form 
<first letter><number><last letter>. 
Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, 
find whether its abbreviation is unique in the dictionary. 
A word's abbreviation is unique if no other word from the dictionary 
has the same abbreviation.

Example: 
Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> 
false

isUnique("cart") -> 
true

isUnique("cane") -> 
false

isUnique("make") -> 
true
"""

class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.map_ = {}
        for item in dictionary:
          if len(item) > 2:
            tmp = item[0] + str(len(item)-2) + item[-1]
          else:
            tmp = item
          if tmp not in self.map_:
            self.map_[tmp] = set([item])
          else:
            self.map_[tmp].add(item)
          # print item, tmp

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) > 2:
          tmp = word[0] + str(len(word)-2) + word[-1]
        else:
          tmp = word
        if tmp not in self.map_: return True
        # print word, tmp
        return len(self.map_[tmp]) == 1 and word in self.map_[tmp]
        # return tmp not in self.set_ 


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)

dictionary = [ "deer", "door", "cake", "card", "internationalization"]
obj = ValidWordAbbr(dictionary)
print obj.isUnique("dear")
print obj.isUnique("cart")
print obj.isUnique("cane")
print obj.isUnique("make")
