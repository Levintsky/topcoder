class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int np = p.size(), ns = s.size();
        vector<int> res;
        if (ns < np)
            return res;
        
        array<int, 26> arr1;
        fill(arr1.begin(), arr1.end(), 0);
        for (int i = 0; i < np; ++i)
            arr1[p[i]-'a']++;
        
        array<int, 26> arr2;
        fill(arr2.begin(), arr2.end(), 0);
        for (int i = 0; i < np; ++i)
            arr2[s[i]-'a']++;
        if (arr1 == arr2)
            res.push_back(0);
        for (int i = np; i < ns; ++i) {
            arr2[s[i]-'a']++;
            arr2[s[i-np]-'a']--;
            if (arr1 == arr2)
                res.push_back(i-np+1);
        }
        return res;
    }
};
