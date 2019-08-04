class Solution {
public:
    void parse(string& s1, vector<string>& v2) {
        int i=0, j=0, vid=0;
        while (i < s1.size()) {
            j = i;
            while (j < s1.size() && s1[j] != ',')
                j++;
            v2[vid++] = s1.substr(i, j-i);
            i = j+1;
        }
    }
    
    vector<string> invalidTransactions(vector<string>& transactions) {
        unordered_map<string, vector<tuple<string, string, string>>> memo;
        vector<vector<string>> trans;
        for (auto& tran : transactions) {
            // istringstream ss(tran);
            vector<string> s(4, "");
            // int i = 0;
            parse(tran, s);
            trans.push_back(s);
        }
        // sort
        sort(trans.begin(), trans.end(), [](const vector<string>& l, const vector<string>& r) {
            return stoi(l[1]) < stoi(r[1]);
        });
        // parse
        for (auto& tran : trans) {
            memo[tran[0]].push_back({tran[1], tran[2], tran[3]});
        }
        unordered_set<string> res;
        for (auto& kv : memo) {
            // kv: (k, [(t1,v1,city1), (t2,v2,city2), ...])
            int i, j;
            string k = kv.first;
            auto& itemlist = kv.second;
            for (i = 0; i < itemlist.size(); ++i)  {
                int t = stoi(get<0>(itemlist[i]));
                int v = stoi(get<1>(itemlist[i]));
                string& city = get<2>(itemlist[i]);
                
                bool flag = false;
                for (j = 0; j < i; ++j) {
                    int t1 = stoi(get<0>(itemlist[j]));
                    string& city1 = get<2>(itemlist[j]);
                    if (t-t1<=60 && city1 != city) {
                        string tmp = k + ',' + get<0>(itemlist[j]);
                        tmp += ',' + get<1>(itemlist[j]);
                        tmp += ',' + get<2>(itemlist[j]);
                        flag = true;
                        res.insert(tmp);
                    }
                }
                if (flag || v > 1000) {
                    string tmp = k + ',' + get<0>(itemlist[i]);
                    tmp += ',' + get<1>(itemlist[i]);
                    tmp += ',' + get<2>(itemlist[i]);
                    res.insert(tmp);
                }
            }
        }
        
        vector<string> result;
        for (string tmp : res)
            result.push_back(tmp);
        sort(result.begin(), result.end());
        return result;
    }
};
