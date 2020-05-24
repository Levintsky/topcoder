class Solution {
public:
    int isPrefixOfWord(string sentence, string searchWord) {
        stringstream is(sentence);
        string s;
        int cnt = 1;
        int n = searchWord.size();
        while (is >> s) {
            if (s.substr(0, n) == searchWord)
                return cnt;
            cnt++;
        }
        return -1;
    }
};
