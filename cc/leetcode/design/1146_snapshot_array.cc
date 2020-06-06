class SnapshotArray {
public:
    vector<vector<int>> arr_t;
    vector<vector<int>> arr_v;
    int tmpid;
    unordered_map<int, int> active_set;
    
    SnapshotArray(int length) {
        arr_t.resize(length, {-1});
        arr_v.resize(length, {0});
        tmpid = 0;
    }
    
    void set(int index, int val) {
        active_set[index] = val;
    }
    
    int snap() {
        for (auto item : active_set) {
            int k = item.first, v = item.second;
            arr_t[k].push_back(tmpid);
            arr_v[k].push_back(v);
        }
        active_set.clear();
        return tmpid++;
    }
    
    int get(int index, int snap_id) {
        // search idx in arr_t[index]
        int idx = 0;
        while (idx < arr_t[index].size() && arr_t[index][idx] <= snap_id)
            idx++;
        idx--;
        return arr_v[index][idx];
    }
};

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray* obj = new SnapshotArray(length);
 * obj->set(index,val);
 * int param_2 = obj->snap();
 * int param_3 = obj->get(index,snap_id);
 */
