class Solution {
public:
    bool isIdealPermutation(vector<int>& A) {
        int n = A.size();
        if (n <= 2)
            return true;
        int n1 = max(A[0], A[1]), n2 = min(A[0], A[1]);
        for (int i = 2; i < n; ++i) {
            if (A[i] > n1) {
                n2 = n1;
                n1 = A[i];
            } else if (A[i] > n2 && A[i-1] > A[i]) {
                n2 = A[i];
            } else
                return false;
        }
        return true;
    }
};

// Smart:
/* The original order should be [0, 1, 2, 3, 4...], the number i should be on the position i. We just check the offset of each number, if the absolute value is larger than 1, means the number of global inversion must be bigger than local inversion, because a local inversion is a global inversion, but a global one may not be local.

proof:

If A[i] > i + 1, means at least one number that is smaller than A[i] is kicked out from first A[i] numbers, and the distance between this smaller number and A[i] is at least 2, then it is a non-local global inversion.
For example, A[i] = 3, i = 1, at least one number that is smaller than 3 is kicked out from first 3 numbers, and the distance between the smaller number and 3 is at least 2.

If A[i] < i - 1, means at least one number that is bigger than A[i] is kicked out from last n - i numbers, and the distance between this bigger number and A[i] is at least 2, then it is a non-local global inversion.
*/

class Solution {
public:
    bool isIdealPermutation(vector<int>& A) {
	for (int i = 0; i < A.size(); ++i) {
            if (abs(A[i] - i) > 1) return false;
        }
	return true;
    }
};
