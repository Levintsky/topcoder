"""
336. Palindrome Pairs (Hard)

Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of
 the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""

"""
Apparently there is an O(n^2 * k) naive solution for this problem, with n the total number of words in the words array 
and k the average length of each word: for each word, we simply go through the words array and check whether the 
concatenated string is a palindrome or not.

Of course this will result in TLE, as expected. To improve the algorithm, we want to reduce the number of words that 
need to be checked for each word, instead of iterating through the whole array. This prompted me to think if I can 
extract any useful information out of the process checking whether the concatenated string is a palindrome, so that 
it can help eliminate as many words as possible for the rest of the words array.

To begin, here is the technique I employed to check for palindromes: maintain two pointers i and j, with i pointing 
to the start of the string and j to the end of the string. Characters pointed by i and j are compared. If at any 
time the characters pointed by them are not the same, we conclude the string is not a palindrome. Otherwise we 
move the two pointers towards each other until they meet in the middle and the string is a palindrome.

By examining the process above, I did find something that we may take advantage of to get rid of words that need to 
be checked otherwise. For example, let's say we want to append words to w0, which starts with character 'a'. Then 
we only need to consider words ending with character 'a', i.e., this will single out all words ending with character 
'a'. If the second character of w0 is 'b', for instance, we can further reduce our candidate set to words ending 
with string "ba", etc. Our naive solution throws away all these useful pieces of information and repeats the 
comparison, which leads to the undesired O(n^2 * k) time complexity.

In order to exploit the information gathered so far, we obviously need to restructure all the words in the words 
array. If you are familiar with Trie structure (I believe you are, since LeetCode has problems for it. In case 
you are not, see Trie), it will come to mind as we need to deal with words with common suffixes. The next step 
is to design the structure for each Trie node. There are at least two fields that should be covered for each 
TrieNode: a TrieNode array denoting the next layer of nodes and a boolean (or integer) to signify the end of 
a word. So our tentative TrieNode will look like this:

class TrieNode {
    TrieNode[] next;
    boolean isWord;
}
One point here is that we assume all the words contain lowercase letters only. This is not specified in the 
problem statement so you probably need to confirm with the interviewer (here I assume it is the case).

Now we will rearrange each word into this Trie structure: for each word, simply starting from its last character 
and identify the node at the next layer by indexing into root's next array with index given by the difference 
between the ending character and character 'a'. If the indexed node is null, create a new node. Continue to the 
next layer and towards the beginning of the word in this manner until we are done with the word, at which point 
we will label the isWord field of the final node as true.

After building up the Trie structure, we can proceed to search for pairs of palindromes for each word in the 
words array. I will use the following example to explain how it works and make possible modifications of the 
TrieNode we proposed above.

Let's say we have these words: ["ba", "a", "aaa"], the Trie structure will be as follows:

        root (f)
           | 'a'
          n1 (t)
     ------------
 'b' |          | 'a'
    n2 (t)    n3 (f)
                | 'a'
              n4 (t)
The letter in parentheses indicates the value of isWord for each node: f ==> false and t ==> true. The letter 
beside each vertical line denotes the index into the next array of the corresponding node. For example, for the 
first vertical line, 'a' means root.next[0] is not null. Similarly 'b' means n1.next[1] is not null, and so on.

Here is the searching process:

For word "ba", starting from the first character 'b', index into the root.next array with index given by 
'b' - 'a' = 1. The corresponding node is null, then we know there are no words ending at this character, so the 
searching process is terminated;
For word "a", again indexing into array root.next at index given by 'a' - 'a' = 0 will yield node n1, which is 
not null. We then check the value of n1.isWord. If it is true, then it is possible to obtain a palindrome by 
appending this word to the one currently being examined (a.k.a word "a"). Also note that the two words should 
be distinct from each other, but the n1.isWord field provides no information about the word itself, which makes 
it impossible to distinguish the two words. So it is necessary to modify the structure of the TrieNode so that 
we can identify the word it represents. One easy way is to have an integer field to remember the index of the 
word in the words array. For non-word nodes, this integer will take negative values (-1 for example) while for 
those representing a word, it will be non-negative values. Suppose we have made this modification, then the two 
words will be identified to be the same, so we discard this pair combination. Since the word "a" has only one 
letter, it seems we are done with it. Or do we? Not really. What if there are words with suffix "a" ("aaa" in 
this case)? We need to continue to check the rest part of these words (such as "aa" for the word "aaa") and see 
if the rest forms a palindrome. If it is, then appending this word ("aaa" in this case) to the original word ("a") 
will also form a palindrome ("aaaa"). Here I take another strategy: add an integer list to each TrieNode; the 
list will record the indices of all words satisfying the following two conditions: 1. each word has a suffix 
represented by the current TrieNode; 2. the rest of the word forms a palindrome.
Before I get to the third word "aaa", let me spell out the new TrieNode and the corresponding Trie structure 
for the above array.

TrieNode:

class TrieNode {
    TrieNode[] next;
    int index;
    List<Integer> list;
            
    TrieNode() {
        next = new TrieNode[26];
        index = -1;
        list = new ArrayList<>();
    }
}
Trie:

          root (-1,[1,2])
            | 'a'
          n1 (1,[0,1,2])
    ---------------------
'b' |                 | 'a'
  n2 (0,[0])    n3 (-1,[2])
                      | 'a'
                 n4 (2,[2])
The first integer in the parentheses is the index of the word in the words" array (defaulted to -1). The integers 
in the square bracket are the indices of words satisfying the two conditions mentioned above.

Let's continue with the third word "aaa" with this new structure. Indexing into array root.next at index given by 
'a' - 'a' = 0 will yield node n1 and n1.index = 1 >= 0, which means we have a valid word now. The index of this 
word (which is 1) is also different from the index of the word currently being visited, a.k.a "aaa" (which is 2). 
So pair (2,1) is a possible concatenation to form a palindrome. But still we need to check the rest of "aaa" 
(excluding the substring represented by current node n1 which is "a" from the beginning of "aaa") to see if it 
is a palindrome. If so, (2,1) will be a valid combination. We continue in this fashion until we reach the end 
of "aaa". Lastly we will check n4.list to see if there are any words satisfying the two conditions specified in 
step 2 which are different from current word, and add the corresponding valid pairs.

Both building and searching the Trie structure take O(n * k^2), which sets the total time complexity of the 
solution. Here is the complete Java program:

private static class TrieNode {
    TrieNode[] next;
    int index;
    List<Integer> list;
      
    TrieNode() {
      next = new TrieNode[26];
      index = -1;
      list = new ArrayList<>();
    }
}
    
public List<List<Integer>> palindromePairs(String[] words) {
    List<List<Integer>> res = new ArrayList<>();

    TrieNode root = new TrieNode();
    
    for (int i = 0; i < words.length; i++) {
        addWord(root, words[i], i);
    }
    
    for (int i = 0; i < words.length; i++) {
        search(words, i, root, res);
    }
    
    return res;
}
    
private void addWord(TrieNode root, String word, int index) {
    for (int i = word.length() - 1; i >= 0; i--) {
        int j = word.charAt(i) - 'a';
        
        if (root.next[j] == null) {
            root.next[j] = new TrieNode();
        }
        
        if (isPalindrome(word, 0, i)) {
            root.list.add(index);
        }
        
        root = root.next[j];
    }
      
    root.list.add(index);
    root.index = index;
}
    
private void search(String[] words, int i, TrieNode root, List<List<Integer>> res) {
    for (int j = 0; j < words[i].length(); j++) { 
      if (root.index >= 0 && root.index != i && isPalindrome(words[i], j, words[i].length() - 1)) {
          res.add(Arrays.asList(i, root.index));
      }
        
      root = root.next[words[i].charAt(j) - 'a'];
        if (root == null) return;
    }
      
    for (int j : root.list) {
      if (i == j) continue;
      res.add(Arrays.asList(i, j));
    }
}
    
private boolean isPalindrome(String word, int i, int j) {
    while (i < j) {
      if (word.charAt(i++) != word.charAt(j--)) return false;
    }
      
    return true;
}
We have the TrieNode structure at the top. In the palindromePairs function, we build up the Trie by adding each word, then search for valid pairs for each word and record the results in the res list. The last isPalindrome function checks if the substring [i, j] (both inclusive) of the given word is a palindrome.

Hope this helps and happy coding!
"""

class Trie():
    def __init__(self):
        self.maps = {}
        self.is_word = False
        self.id_ = -1

class TrieNode(object):
    def __init__(self):
        self.next = [None] * 26
        self.index = -1
        self.lists = []

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # add every word into a Trie
        root = Trie()
        for ii in range(len(words)):
          word = words[ii]
          node = root
          if word == '':
            node.is_word = True
            # node.ids.append(ii)
            node.id_ = ii
          for i in range(len(word)):
            c = word[i]
            if c not in node.maps:
              node.maps[c] = Trie()
            # node.ids.append(ii)
            node = node.maps[c]
            if i == len(word)-1: # last character
              node.is_word = True
              # node.ids.append(ii)
              node.id_ = ii
        result = []

        def traverse(node, prefix, ii):
          if node.is_word and self.is_palin(prefix) and node.id_!=ii:
            result.append([node.id_, ii])
          for c in node.maps:
            traverse(node.maps[c], prefix+c, ii)

        for ii in range(len(words)):
          word = words[ii]
          word = word[::-1]
          node = root
          if root.is_word:
            if self.is_palin(word) and ii != node.id_:
              # print word, ii
              result.append([node.id_, ii])
              # print result
              result.append([ii, node.id_])
              # print result
          # look up first
          for i in range(len(word)):
            c = word[i]
            if c not in node.maps: break
            node = node.maps[c]
            if node.is_word: # is_word
              # check word[i+1..]
              tmp = word[i+1:]
              if self.is_palin(tmp) and ii != node.id_:
                result.append([node.id_, ii])
            if i == len(word)-1:
                traverse(node, '', ii)

        print(result)
        result = set([tuple(item) for item in result])
        result = list(result)
        result = [list(item) for item in result]
        return result

    def is_palin(self, word):
        i = 0
        j = len(word) - 1
        while i < j and word[i] == word[j]:
            i += 1
            j -= 1
        if i >= j: return True
        else: return False

    def solve2(self, words):
        self.root = TrieNode()

        def subPalin(word, i, j):
            while i < j:
                if word[i] == word[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True

        def addWord(word, index):
            # add reverse of each word in the trie
            # key preprocessing step: check if [0:i] is palindrome
            root = self.root
            for i in range(len(word)-1, -1, -1):
                j = ord(word[i]) - ord('a')
                if root.next[j] is None:
                    root.next[j] = TrieNode()
                if subPalin(word, 0, i):
                    root.lists.append(index)
                root = root.next[j]
            root.lists.append(index)
            root.index = index
            return

        for i, word in enumerate(words):
            addWord(word, i)

        self.result = []
        def search(word, i):
            root = self.root
            n = len(word)
            for j in range(n):
                if root.index >= 0 and root.index != i and subPalin(word, j, n-1):
                    self.result.append([i, root.index])
                ind = ord(word[j]) - ord('a')
                if root.next[ind] is None:
                    return
                root = root.next[ind]

            for j in root.lists:
                if i == j:
                    continue
                self.result.append([i, j])
            return

        for i, word in enumerate(words):
            search(word, i)

        return self.result

    def solve3(self, words):
        d = {}
        for i, word in enumerate(words):
            d[word[::-1]] = i
        ans = []
        for idx, word in enumerate(words):
            for i in range(len(word)):
                l = word[:i]
                r = word[i:]
                # word = left + right, check
                # 1. left[::-1] in memo dictionary
                # 2. right is palindrome
                # then word::left[::-1] is a solution
                # special case: left is "", [l, idx]
                if l in d and idx != d[l] and r[::-1] == r:
                    ans.append([idx, d[l]])
                    if not l:
                        ans.append([d[l], idx])
                # 1. left is palindrome
                # 2. right[::-1] :: left :: right is palindrome
                # special case: right == ""
                if r in d and idx != d[r] and l[::-1] == l:
                    ans.append([d[r], idx])
                    if not r:
                        ans.append([idx, d[r]])
        return ans


if __name__ == "__main__":
  a = Solution()
  """
  print(a.palindromePairs(["ba", "abc"]))
  print(a.palindromePairs(["bat", "tab", "cat"]))
  print(a.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
  print(a.palindromePairs(["a", "", "aa"]))
  print(a.palindromePairs(["a","b","c","ab","ac","aa"]))
  print(a.palindromePairs(["a","ab","ac"]))
  """
  print(a.solve3(["aa", "aabb"]))
