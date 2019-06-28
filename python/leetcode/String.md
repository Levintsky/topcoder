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

## Suffix Array
- https://www.geeksforgeeks.org/suffix-array-set-1-introduction/
- Definition: sorted of all suffixes of a given string;
- e.g. Banana, sorted suffixes:
	- 5 a
	- 3 ana
	- 1 anana
	- 0 banana
	- 4 na
	- 2 nana
- Step 2: construct lcp array (Kasai algorithm), longest common prefix between suffix[i] and suffix[i+1]
```c++
/* To construct and return LCP */
vector<int> kasai(string txt, vector<int> suffixArr) 
{ 
    int n = suffixArr.size(); 
  
    // To store LCP array 
    vector<int> lcp(n, 0); 
  
    // An auxiliary array to store inverse of suffix array 
    // elements. For example if suffixArr[0] is 5, the 
    // invSuff[5] would store 0.  This is used to get next 
    // suffix string from suffix array. 
    vector<int> invSuff(n, 0); 
  
    // Fill values in invSuff[] 
    for (int i=0; i < n; i++) 
        invSuff[suffixArr[i]] = i; 
  
    // Initialize length of previous LCP 
    int k = 0; 
  
    // Process all suffixes one by one starting from 
    // first suffix in txt[] 
    for (int i=0; i<n; i++) 
    { 
        /* If the current suffix is at n-1, then we don’t 
           have next substring to consider. So lcp is not 
           defined for this substring, we put zero. */
        if (invSuff[i] == n-1) 
        { 
            k = 0; 
            continue; 
        } 
  
        /* j contains index of the next substring to 
           be considered  to compare with the present 
           substring, i.e., next string in suffix array */
        int j = suffixArr[invSuff[i]+1]; 
  
        // Directly start matching from k'th index as 
        // at-least k-1 characters will match 
        while (i+k<n && j+k<n && txt[i+k]==txt[j+k]) 
            k++; 
  
        lcp[invSuff[i]] = k; // lcp for the present suffix. 
  
        // Deleting the starting character from the string. 
        if (k>0) 
            k--; 
    } 
  
    // return the constructed lcp array 
    return lcp; 
} 
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
    - LC-132: Palindrome Partitioning II
