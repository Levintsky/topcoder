class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        vector<string> table = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        unordered_set<string> memo;
        for (string& word : words) {
            string tmp;
            for (char c : word) {
                tmp += table[c-'a'];
            }
            memo.insert(tmp);
        }
        return memo.size();
    }
};
