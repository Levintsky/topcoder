class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        static int fast_io = []() { std::ios::sync_with_stdio(false); cin.tie(nullptr);
                                    return 0; }();                                   
        auto res = upper_bound(letters.begin(), letters.end(), target);
        if (res == letters.end())
            return letters[0];
        else
            return *res;
    }
};
