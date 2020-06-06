"""
271. Encode and Decode Strings (Medium)

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

Note:
The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.
"""

class Codec:
  def encode(self, strs):
    """Encodes a list of strings to a single string.
        
    :type strs: List[str]
    :rtype: str
    """
    # encode as len(strs)
    # then len(str[0]), len(str[1]), ...
    # then strs
    res = ""
    n = len(strs)
    res += str(n) + " "
    if n > 0:
      for i in range(n):
        res += str(len(strs[i])) + " "
      for i in range(n):
        res += strs[i]
    return res
        

  def decode(self, s):
    """Decodes a single string to a list of strings.
        
    :type s: str
    :rtype: List[str]
    """
    ret = []
    if s[0] == "0": return ret
    # step 1: get n
    i = 0
    n = 0
    while s[i] != ' ':
      n = n * 10 + ord(s[i]) - ord('0')
      i += 1
    print 'n:', n
    i += 1
    len_list = []
    for idx in range(n):
      tmp = 0
      while s[i] != ' ': 
        tmp = tmp * 10 + ord(s[i]) - ord('0')
        i += 1
      len_list.append(tmp)
      i += 1
    print 'len list:', len_list
    for idx in range(n):
      ret.append(s[i:i+len_list[idx]])
      i += len_list[idx]
    return ret

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

if __name__ == "__main__":
  codec = Codec()
  strs = ["abc", "d", "ef", "", "ggg"]
  res = codec.encode(strs)
  print res
  ret = codec.decode(res)
  print ret
