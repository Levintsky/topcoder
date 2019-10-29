
class Node {
public:
    Node() {end=false;}
    unordered_map<string, Node*> memo;
    bool end;
};

class Solution {
public:
    struct less_key {
        bool operator() (const string& s1, const string& s2) {
            return s1.size() < s2.size();
        }
    };
    
    void parse(string& s, vector<string>& dir) {
        int i = 0, j;
        while (i < s.size()) {
            if (s[i] == '/')
                i++;
            j = i;
            while (j < s.size() && s[j] != '/')
                j++;
            dir.push_back(s.substr(i, j-i));
            i = j + 1;
        }
    }
    
    vector<string> removeSubfolders(vector<string>& folder) {
        // sort by length
        sort(folder.begin(), folder.end(), less_key());
        
        vector<string> result;
        Node* root = new Node();
        Node* n;
        for (string& s : folder) {
            vector<string> tmp;
            parse(s, tmp);
            /*cout << s <<":";
            for (int i = 0; i < tmp.size(); ++i)
                cout << tmp[i] << " ";
            cout << endl;*/
            bool flag = true;
            n = root;
            for (int i = 0; i < tmp.size(); ++i) {
                if (n->end) {
                    flag = false;
                    break;
                }
                string item = tmp[i];
                if (n->memo.find(item) == n->memo.end())
                    n->memo[item] = new Node();
                n = n->memo[item];
                if (i == tmp.size() - 1)
                    n->end = true;
            }
            if (flag)
                result.push_back(s);
        }
        
        return result;
    }
};
