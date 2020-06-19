class UndergroundSystem {
public:
    unordered_map<int, pair<string, int>> memo_id;
    unordered_map<string, vector<int>> memo_record;
        
    UndergroundSystem() {
        
    }
    
    void checkIn(int id, string stationName, int t) {
        memo_id[id] = make_pair(stationName, t);
    }
    
    void checkOut(int id, string stationName, int t) {
        string s1 = memo_id[id].first;
        string s2 = stationName;
        string key = s1 + '#' + s2;
        memo_record[key].push_back(t - memo_id[id].second);
    }
    
    double getAverageTime(string startStation, string endStation) {
        string key = startStation + '#' + endStation;
        double res = 0.;
        for (int item : memo_record[key])
            res += item;
        res /= memo_record[key].size();
        return res;
    }
};

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */