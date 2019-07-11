'''
299. Bulls and Cows (Medium)

You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

For example:

Secret number:  "1807"
Friend's guess: "7810"
Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)
Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. In the above example, your function should return "1A3B".

Please note that both secret number and friend's guess may contain duplicate digits, for example:

Secret number:  "1123"
Friend's guess: "0111"
In this case, the 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow, and your function should return "1A1B".
You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
'''
import collections


class Solution(object):
    def getHint(self, secret, guess):
        n = len(secret)
        if n == 0:
            return ''

        s1 = dict(collections.Counter(secret))
        s2 = dict(collections.Counter(guess))

        # count
        cnt = 0
        for k in s1:
            if k in s2:
                cnt += min(s1[k], s2[k])

        cnt2 = 0
        for i in range(n):
            if secret[i] == guess[i]:
                cnt2 += 1

        return str(cnt2)+'A'+str(cnt-cnt2)+'B'

    def solve2(self, secret, guess):
        memo_s = {}
        memo_g = {}
        A, B = 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                memo_s[secret[i]] = memo_s.get(secret[i], 0) + 1
                memo_g[guess[i]] = memo_g.get(guess[i], 0) + 1
        # check B
        for k in memo_s.keys():
            if k in memo_g:
                B += min(memo_s[k], memo_g[k])
        s = "%dA%dB" % (A, B)
        return s

if __name__ == '__main__':
  a = Solution()
  print(a.getHint('1123', '0111'))
