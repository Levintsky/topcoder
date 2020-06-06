"""
642. Design Search Autocomplete System (Hard)

Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, then just return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
Your job is to implement the following functions:

The constructor function:

AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. Your system should record these historical data.

Now, the user wants to input a new sentence. The following function will provide the next character the user types:

List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.

Example:
Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2]) 
The system have already tracked down the following sentences and their corresponding times: 
"i love you" : 5 times 
"island" : 3 times 
"ironman" : 2 times 
"i love leetcode" : 2 times 
Now, the user begins another search: 

Operation: input('i') 
Output: ["i love you", "island","i love leetcode"] 
Explanation: 
There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored. 

Operation: input(' ') 
Output: ["i love you","i love leetcode"] 
Explanation: 
There are only two sentences that have prefix "i ". 

Operation: input('a') 
Output: [] 
Explanation: 
There are no sentences that have prefix "i a". 

Operation: input('#') 
Output: [] 
Explanation: 
The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search. 

Note:
The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words.
The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100.
Please use double-quote instead of single-quote when you write test cases even for a character input.
Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are persisted across multiple test cases. Please see here for more details.
"""
class Trie(object):
  def __init__(self):
    self.child = {}
    self.is_end = False

class AutocompleteSystem(object):
  def __init__(self, sentences, times):
    """
    :type sentences: List[str]
    :type times: List[int]
    """
    self.data = {} # sentence to time mapping
    n = len(times)
    for i in range(n):
      self.data[sentences[i]] = times[i]
    self.root = Trie()
    self.curr = self.root
    self.flag = True # if qeury is searchable or not
    self.query = "" # keep a record of current query

    for item in self.data.keys():
      # add to Trie
      node = self.root
      for i in range(len(item)):
        c = item[i]
        if c not in node.child:
          node.child[c] = Trie()
        node = node.child[c]
        if i == len(item)-1:
          node.is_end = True

  def helper(self, node, prefix):
    # return all strings starting from current node
    # add prefix
    result = []
    while True:
      if node.is_end:
        result.append(prefix)
      if len(node.child) == 0:
        break
      elif len(node.child) == 1:
        c = node.child.keys()[0]
        prefix = prefix + c
        node = node.child[c]
      else: # more than one child
        for c in node.child.keys():
          result += self.helper(node.child[c], prefix+c)
        break
    return result

  def reset(self):
    # reset status
    self.query = ""
    self.flag = True
    self.curr = self.root

  def input(self, c):
    """
    :type c: str
    :rtype: List[str]
    """
    # if query ends with a '#'
    sharp_flag = c=='#'

    if not sharp_flag: # not ending
      self.query += c
      if not self.flag: # already not found
        return []
      elif c not in self.curr.child: # current c not found
        self.flag = False
        return []
      else:
        self.curr = self.curr.child[c]
        result = self.helper(self.curr, self.query) # get all result
        # ranking and keep top 3
        result = [(self.data[item], item) for item in result]
        result.sort(key= lambda item: (-item[0],item[1]))
        result = [item[1] for item in result]
        result = result[:3]
        return result
    else: # end with '#'
      if self.query in self.data: # query found, return all result
        self.data[self.query] += 1
        '''result = self.helper(self.curr, self.query) # get all result
        # ranking and keep top 3
        result = [(self.data[item], item) for item in result]
        result.sort(key= lambda item: (-item[0],item[1]))
        result = [item[1] for item in result]
        result = result[:3]'''
        self.reset()
        # return result
      else:
        self.data[self.query] = 1
        # add self.query to the system
        node = self.root
        for i in range(len(self.query)):
          c = self.query[i]
          if c not in node.child:
            node.child[c] = Trie()
          node = node.child[c]
          if i == len(self.query)-1:
            node.is_end = True
        self.reset()
      return []


if __name__ == '__main__':
  sentences = ["i love you", "island", "ironman", "i love leetcode"]
  times = [5,3,2,2]
  # sentences = ['i love']
  # times = [2]

  acs = AutocompleteSystem(sentences, times)
  # print acs.helper(acs.root, "")
  print acs.input("i")
  print acs.input(" ")
  print acs.input("a")
  print acs.input("#")
  print acs.input("i")
  print acs.input(" ")
  print acs.input("a")
  print acs.input("#")
  print acs.input("i")
  print acs.input(" ")
  print acs.input("a")
  print acs.input("#")
# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
