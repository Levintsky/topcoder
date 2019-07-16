class Solution {
public:
    vector<int> distributeCandies(int candies, int np) {
        vector<int> res(np, 0);
        int base = 1;
        int i = 0;
        int give;
        while (candies > 0) {
            if (candies > base) {
                res[i] += base;
                candies -= base;
                base++;
                i = (i + 1) % np;
            } else {
                res[i] += candies;
                break;
            }
        }
        return res;
    }
};
