/*
The big idea is pretty simple:
Each time of book, instead of fail a book when there is 1 or more overlap with existing books as in MyCalendar I, we just want to make sure these overlaps does not overlap - having overlap is now ok, but overlapped period cannot be overlapped again.
So we just need to keep track of all the overlaps with any previous books

MyCalendar I can be reused to track the overlaps during each book.

How to calculate overlap of 2 intervals
Assume a start earlier than b, (if not reverse), there could be 3 case, but in any case, an overlap(either positive or negative) can always be represented as:
(max(a0, b0), min(a1, b1))

case 1: b ends before a ends:
a: a0 |-------------| a1
b:     b0 |-----| b1

case 2: b ends after a ends:
a: a0 |--------| a1
b:     b0 |--------| b1

case 3: b starts after a ends: (negative overlap)
a: a0 |----| a1
b:              b0 |----| b1
Java
*/

class MyCalendarTwo {
    private List<int[]> books = new ArrayList<>();    
    public boolean book(int s, int e) {
        MyCalendar overlaps = new MyCalendar();
        for (int[] b : books)
            if (Math.max(b[0], s) < Math.min(b[1], e)) // overlap exist
                if (!overlaps.book(Math.max(b[0], s), Math.min(b[1], e))) return false; // overlaps overlapped
        books.add(new int[]{ s, e });
        return true;
    }

    private static class MyCalendar {
        List<int[]> books = new ArrayList<>();
        public boolean book(int start, int end) {
            for (int[] b : books)
                if (Math.max(b[0], start) < Math.min(b[1], end)) return false;
            books.add(new int[]{ start, end });
            return true;
        }
    }
}

// C++

class MyCalendar {
    vector<pair<int, int>> books;
public:
    bool book(int start, int end) {
        for (pair<int, int> p : books)
            if (max(p.first, start) < min(end, p.second)) return false;
        books.push_back({start, end});
        return true;
    }
};

class MyCalendarTwo {
    vector<pair<int, int>> books;
public:
    bool book(int start, int end) {
        MyCalendar overlaps;
        for (pair<int, int> p : books) {
            if (max(p.first, start) < min(end, p.second)) { // overlap exist
                pair<int, int> overlapped = getOverlap(p.first, p.second, start, end);
                if (!overlaps.book(overlapped.first, overlapped.second)) return false; // overlaps overlapped
            }
        }
        books.push_back({ start, end });
        return true;
    }

    pair<int, int> getOverlap(int s0, int e0, int s1, int e1) {
        return { max(s0, s1), min(e0, e1)};
    }
};

/*
Another way to calculate overlap of 2 intervals
a started with b, or, b started within a:

a:                     |---------|
b:
a0<b0 & a1<b0:  |----|
a0<b0 & a1>b0:  |------------| (a started within b)
a0<b0 & a1>b1:  |-------------------| (a started within b)
a0>b0 & a0<b1:            |----|  (b started within a)
a0>b0 & a0>b1:            |---------| (b started within a)
a0>b1 & a1>b1:                      |----|
*/
