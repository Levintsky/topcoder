"""
205. Isomorphic Strings (Easy)

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving 
the order of characters. No two characters may map to the same character but a character 
may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        num = len(s)
        map_s2t = {}
        map_t2s = {}
        for i in range(num):
            if map_s2t.has_key(s[i]):
                if t[i] != map_s2t[s[i]]:
                    return False
            else:
                map_s2t[s[i]] = t[i]
            if map_t2s.has_key(t[i]):
                if s[i] != map_t2s[t[i]]:
                    return False
            else:
                map_t2s[t[i]] = s[i]
        return True
