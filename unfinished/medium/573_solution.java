/*
Proof: Let the minimum distance from each nut to the tree be a_1, ..., a_n and let the minimum distance from each nut to the initial squirrel position be b_1, ..., b_n. Note that the minimum distance between two positions in the matrix is determined by their Manhattan distance.

Then, if the squirrel were to start at the tree, then the minimum total distance required to collect all the nuts is 2a_1 + ... + 2a_n. However, since the squirrel starts elsewhere, we just need to substitute one of the 2a_i terms with a_i + b_i. Or equivalently, we replace one of the a_i terms in the sum with b_i. To minimize the total sum value at the end, we choose i that maximizes a_i - b_i.
*/

public int minDistance(int height, int width, int[] tree, int[] squirrel, int[][] nuts) {
    int sum = 0, maxDiff = Integer.MIN_VALUE;
    for (int[] nut : nuts) {
        int dist = Math.abs(tree[0] - nut[0]) + Math.abs(tree[1] - nut[1]);
        sum += 2*dist;
        maxDiff = Math.max(maxDiff, dist - Math.abs(squirrel[0] - nut[0]) - Math.abs(squirrel[1] - nut[1]));
    }
    return sum - maxDiff;
}
