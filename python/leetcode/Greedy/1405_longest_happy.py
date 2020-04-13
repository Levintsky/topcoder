"""
1405. Longest Happy String (Medium)

A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.

Given three integers a, b and c, return any string s, which satisfies following conditions:

s is happy and longest possible.
s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
s will only contain 'a', 'b' and 'c' letters.
If there is no such string s return the empty string "".

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 2, b = 2, c = 1
Output: "aabbc"
Example 3:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It's the only correct answer in this case.

Constraints:

0 <= a, b, c <= 100
a + b + c > 0
"""

"""
Solution:
Tip: to simplify the logic, preprocess to assume a >= b >= c.

Update: I added the code with different variable names: lg, med and sm, and we preprocess so that lg >= med >= sm. Perhaps, it's easier to understand. See "Same Approach, Different Names" below.

Intuition: this is almost identical to 984. String Without AAA or BBB. We just need to ignore the smallest count in each round. Aassuming a >= b >= c: always try to add 'aa'. If a - 2 >= b, add 'b' (if not, the next round will add 'bb'). Repeat recursivelly for the remaining counts.

In other words, we are greedily use two characters from the largest pile. We cusion these two characters with a character from the medium pile. For [11,5,3], as an example, we first generate 'aabaabaab', and our piles become [5,2,3]. At this time, c becomes the medium pile, and we generate '..aac' ([3,2,2]). After we add one more '..aa', c becomes the largest pile and we pull two characters from it '..cc' ([1,2,0]). We add the rest '..bba', and the resulting string is 'aabaabaabaacaaccbba'.

This algorithm can be esilly proved to be correct by a contradiction (and counter-examples).

C++

string longestDiverseString(int a, int b, int c, char aa = 'a', char bb = 'b', char cc = 'c') {
    if (a < b)
        return longestDiverseString(b, a, c, bb, aa, cc);
    if (b < c)
        return longestDiverseString(a, c, b, aa, cc, bb);
    if (b == 0)
        return string(min(2, a), aa);
    auto use_a = min(2, a), use_b = a - use_a >= b ? 1 : 0; 
    return string(use_a, aa) +  string(use_b, bb) + 
        longestDiverseString(a - use_a, b - use_b, c, aa, bb, cc);
}
Java

String generate(int a, int b, int c, String aa, String bb, String cc) {
    if (a < b)
        return generate(b, a, c, bb, aa, cc);
    if (b < c)
        return generate(a, c, b, aa, cc, bb);
    if (b == 0)
        return aa.repeat(Math.min(2, a));
    int use_a = Math.min(2, a), use_b = a - use_a >= b ? 1 : 0; 
    return aa.repeat(use_a) + bb.repeat(use_b) +
        generate(a - use_a, b - use_b, c, aa, bb, cc);    
}
public String longestDiverseString(int a, int b, int c) {
    return generate(a, b, c, "a", "b", "c");
}
Same Approach, Different Names
string longestDiverseString(int lg, int med, int sm, char ch_lg = 'a', char ch_med = 'b', char ch_sm = 'c') {
    if (lg < med)
        return longestDiverseString(med, lg, sm, ch_med, ch_lg, ch_sm);
    if (med < sm)
        return longestDiverseString(lg, sm, med, ch_lg, ch_sm, ch_med);
    if (med == 0)
        return string(min(2, lg), ch_lg);
    auto use_lg = min(2, lg), use_med = lg - use_lg >= med ? 1 : 0; 
    return string(use_lg, ch_lg) +  string(use_med, ch_med) + 
        longestDiverseString(lg - use_lg, med - use_med, sm, ch_lg, ch_med, ch_sm);
}
"""

class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        l = [a,b,c]
        l.sort(reverse=True)
        max_, mid_, min_ = l[0], l[1], l[2]
        l[0] = min(l[0], 2*(l[1]+l[2]+1))
        res = []

        while l[0] > 0:
            if l[0] >= 2*(l[1]+l[2]):
                if l[0] >= 2:
                    res += [0, 0]
                    l[0] -= 2
                else:
                    res.append(0)
                    l[0] -= 1

                if l[1] > 0:
                    res.append(1)
                    l[1] -= 1
                elif l[2] > 0:
                    res.append(2)
                    l[2] -= 1
            else:
                res.append(0)
                l[0] -= 1
                if l[2] > 0:
                    l[2] -= 1
                    res.append(2)
                elif l[1] > 0:
                    l[1] -= 1
                    res.append(1)
        # if extra l[1]
        print(res)
        res2 = []
        if l[1] > 0:
            for item in res:
                if l[1] > 0 and (len(res2) == 0 or res2[-1] != 1):
                    res2.append(1)
                    l[1] -= 1
                res2.append(item)
        else:
            res2 = res
        print(res2)
        l = [(a, 'a'),(b, 'b'),(c, 'c')]
        l.sort(reverse=True)
        res3 = ""
        for item in res2:
            res3 += l[item][1]
        return res3


if __name__ == "__main__":
    a = Solution()
    # print(a.longestDiverseString(1, 1, 7))
    # print(a.longestDiverseString(2, 2, 1))
    print(a.longestDiverseString(1, 0, 3))
