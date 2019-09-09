"""
1189. Maximum Number of Balloons (Easy)

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:

Input: text = "nlaebolko"
Output: 1
Example 2:

Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
"""

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        target = 'balloon'
        target_memo, text_memo = [0] * 26, [0] * 26
        def stat_text(txt, memo):
            for c in txt:
                idx = ord(c) - ord('a')
                memo[idx] += 1
        
        stat_text(target, target_memo)
        stat_text(text, text_memo)
        res = None
        for i in range(26):
            if target_memo[i] == 0:
                continue
            tmp = text_memo[i] // target_memo[i]
            if res is None:
                res = tmp
            else:
                res = min(res, tmp)
        return res