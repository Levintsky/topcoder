"""
937. Reorder Log Files (Easy)

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
 

Note:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
"""

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digit = []
        letters = []
        for log in logs:
            data = log.split()
            try:
                _ = int(data[1])
                digit.append(log)
            except ValueError:
                letters.append(data)
        # sort the letters alphabetically
        print(letters)
        letters = [tuple(item[1:]+[item[0]]) for item in letters]
        letters.sort()
        letters = [list(item) for item in letters]
        letters = [" ".join([item[-1]] + item[:-1]) for item in letters]
        for log in digit:
            letters.append(log)
        return letters


if __name__ == "__main__":
    a = Solution()
    print(a.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
