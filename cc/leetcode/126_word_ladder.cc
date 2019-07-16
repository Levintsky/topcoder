class Solution {
public:
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> dic(wordList.begin(), wordList.end());
        unordered_map<string, unordered_set<string> > memo;
        dic.insert(beginWord);
        vector<vector<string> > result;
        if (wordList.size() == 0)
        	return result;
        int wordn = wordList[0].size();

        for (auto word1 : wordList) {
        	for (int i = 0; i < wordn; i++) {
        		string word2(word1);
        		for (char c = 'a'; c <= 'z'; ++c) {
        			word2[i] = c;
        			if (word1 != word2 && dic.find(word2) != dic.end()) {
        				memo[word1].insert(word2);
        				memo[word2].insert(word1);
        			}
        		}
        	}
        }

        result.push_back({endWord});
        vector<vector<string> > new_res;
        while (result && result[0][-1] != beginWord) {
        	for (auto tmpvec : result) {
        		vector<string> newvec(tmpvec);
	        	string lastword = tmpvec[tmpvec.size()-1];
        		for (auto par : memo[lastword]) {
        			newvec.push_back(par);
        			new_res.push_back(newvec);
        		}
        	}
        	swap(result, new_res);
        	new_res.clear();
        }
        for (auto& item : result)
        	reverse(item.begin(), item.end());
        return result;
    }
};