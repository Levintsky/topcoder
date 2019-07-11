"""
819. Most Common Word (Easy)

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

 

Example:

Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
 

Note:

1 <= paragraph.length <= 1000.
0 <= banned.length <= 100.
1 <= banned[i].length <= 10.
The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
There are no hyphens or hyphenated words.
Words only consist of letters, never apostrophes or other punctuation symbols.
"""


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        def isChar(c):
            res1 = ord(c) >= ord('a') and ord(c) <= ord('z')
            res2 = ord(c) >= ord('A') and ord(c) <= ord('Z')
            return res1 or res2

        memo = {}
        words = []
        curr = ""
        for i, c in enumerate(paragraph):
            if isChar(c):
                curr += c.lower()
                if i == len(paragraph) - 1:
                    words.append(curr)
            else:
                if curr != "":
                    words.append(curr)
                    curr = ""
        print(words)

        for item in words:
            item = item.replace(".", "")
            item = item.replace(",", "")
            item = item.replace("!", "")
            item = item.lower()
            memo[item] = memo.get(item, 0) + 1
        # print(memo)
        # inv
        memo_inv = {}
        v_max = 0
        for k, v in memo.items():
            if v not in memo_inv:
                memo_inv[v] = []
            memo_inv[v].append(k)
            v_max = max(v_max, v)
        # print(memo_inv)
        for vv in range(v_max, 0, -1):
            if vv in memo_inv:
                for k in memo_inv[vv]:
                    if k not in banned:
                        return k

    def solve2(self, paragraph, banned):
    	banned = set(banned)
        
        maxWord = None
        maxCount = float('-inf')
        paragraph = paragraph.replace(",", " ")
        
        collection = {}
        
        for word in paragraph.split():
            word = word.lower().strip("!?',;.")
            if word not in banned:
                if word in collection:
                    collection[word] += 1
                else:
                    collection[word] = 1
            
                if collection[word] > maxCount:
                    maxCount = collection[word]
                    maxWord = word
        
        return maxWord


if __name__ == "__main__":
    a = Solution()
    print(a.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
    print(a.mostCommonWord("Bob!", ['hit']))
    print(a.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))
