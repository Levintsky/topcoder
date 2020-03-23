# String Tricks

## Pattern Searching
- KMP
- Rain Karp
- Finite Automata
- Boyer Moore
- Suffix Tree
	- Costly if text changes

## Suffix Tree
- https://blog.csdn.net/SunnyYoona/article/details/43971087
- Intro:
	- https://www.geeksforgeeks.org/pattern-searching-using-suffix-tree/
- A Trie containing all suffix:
	- eg. "banana" -> banana, anana, nana, ana, na, a, ...
- Applications:
	- Pattern searching;
	- Find how many times a substr appears;
	- Find longest repeated substring; (1044)
	- Find longest common substring: S1#S2 and check;
	- Longest palindrome;
- Ukkonen’s Suffix Tree Construction;
    - Edge: string;
    - Node: active index;

## Suffix Array
- Typical problems:
    - **LC-1044**: Longest Duplicate Substring
- Definition: sorted of all suffixes of a given string;
- e.g. Banana, sorted suffixes:
    - 5 a
    - 3 ana
    - 1 anana
    - 0 banana
    - 4 na
    - 2 nana
- Construction:
    - Introduction, Naive method
        - https://www.geeksforgeeks.org/suffix-array-set-1-introduction/
        - Sort all suffixes, keep indexes O(n^2 logn)
    - Better: O(n logn^2)
        - Sort according to first 2 char, then 4
        - https://www.geeksforgeeks.org/suffix-array-set-2-a-nlognlogn-algorithm/
- Step 2: construct lcp array (Kasai algorithm), longest common prefix between suffix[i] and suffix[i+1], take "mississippi" as an example
    - 2.1 suffix array: [10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2], (sorted alphabetical)
    - 2.2 inv suffix array: [4, 3, 10, 8, 2, 9, 7, 1, 6, 5, 0], (sorting index for each suffix)
    - 2.3 go through inv_suf[i], compared with real next
    - 2.3.1 "mississippi" (rank the 4th) and find the 5th "pi", lcp[4]= 0
    - 2.3.2 "ississippi" (3rd), find 4th "mi", lcp[3] = 0
    - 2.3.3 "ssissippi" (last), no next, skip, lcp[10] = 0 not changed
    - 2.3.4 "sissippi" (8th), with 9th "ssippi", lcp[8] = 1, k = 1
    - 2.3.5 "issippi" (2nd), with 3rd suffix[3]=1, "ississippi", lcp[2] = 4
    ```python
    def kasai(txt, suffixArr):
        n = len(suffixArr)
        lcp = [0] * n
        invSuff = [0] * n

        for i in range(n):
            invSuff[suffixArr[i]] = i

        k = 0
        for i in range(n):
            if invSuff[i] == n - 1:
                k = 0
                continue
            j = suffixArr[invSuff[i] + 1]
            while i + k < n and j + k < n and txt[i + k] == txt[j + k]:
                k += 1

            lcp[invSuff[i]] = k
            if k > 0:
                k -= 1
        return lcp
    ```

	- https://www.geeksforgeeks.org/%C2%AD%C2%ADkasais-algorithm-for-construction-of-lcp-array-from-suffix-array/
	- lcp[0] = 1, 'a', 'ana'
	- lcp[1] = 3, 'ana', 'anana'
	- lcp[2] = 0
	- lcp[3] = 0
	- lcp[4] = 2, 'na', 'nana'
	- lcp[5] = 0

## Palindrome
- Typical questions:
    - LC-131: Palindrome Partitioning
    - LC-132: Palindrome Partitioning II
    - LC-214: Shortest Palindrome
    - LC-336: Palindrome Pairs
    - **LC-516**: Longest Palindromic Subsequence
        - DP: O(n^2)
        - i from n-1..0
        -     dp[i,j] := best result of s[i,j]
        -     dp[j] = dp[i+1,j-1] + 2 (if s[i] == s[j])
        -             max(dp[i,j-1], dp[i+1,j]), otherwise

## Minimum Edit
- Typical questions:
    - LC-316: Remove Duplicate Letters
    - LC-420: Strong Password Checker
    - LC-664: Strange Printer
    - LC-32: Longest Valid Parentheses
    - **LC-301**: Remove Invalid Parentheses (harder version of LC-32, DFS)

## Substring
- LC-583: Delete Operation for Two Strings
- LC-516: Longest Palindromic Subsequence
- Continuous:
    - **LC-1163**: Last Substring in Lexicographical Order
        - Think naively, no need to always go with suffix array!

## Matching
- LC-10: Regular Expression Matching (with . and \*)
- LC-44: Wildcard Matching

## Parsing
- Generally, stack is used! or solve recursively. Interal tree structure.
- **LC-224**: Basic Calculator
- **LC-227**: Basic Calculator II
- LC-388: Longest Absolute File Path
- **LC-772**: **Basic Calculator III
- **LC-770**: Basic Calculator IV
- LC-1106: Parsing A Boolean Expression
- State machine:
    - String to Integer (atoi)
    - LC-65: Valid Number
- LC-1111: Maximum Nesting Depth of Two Valid Parentheses Strings
- LC-1003: Check If Word Is Valid After Substitutions

## Misc
- Sorting Alphabetical:
    - LC-179: Largest Number
    - LC-440: K-th Smallest in Lexicographical Order
- LC-459: Repeated Substring Pattern
- LC-466: Count The Repetitions
- **Rolling Hash**:
    - LC-1392: Longest Happy Prefix;
