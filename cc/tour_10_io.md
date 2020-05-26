# Input and Output (Chap 10 of a Tour of C++)

## Overview
- Introduction
- Output
- Input
- I/O State
- I/O of User-Defined Types
- Formatting
- File Streams
- String Streams
- C-style I/O
- File System

## I/O State
- Get input by lines: then run ./executable < textfile
```cpp
// read input a line at a time and discard blank lines 
while (getline(cin, line))
	if (!line.empty())
		cout << line << endl;
```
- Read until non-integer (e.g., 'a');
	- is>>i returns a reference to is, and testing an iostream yields true if the stream is ready for another operation.
```cpp
vector<int> read_ints(istream& is) {
     vector<int> res;
     for (int i; is>>i; )
           res.push_back(i);
    return res;
}
```

## User-Defined I/O
- Specify a {"name",number} format;
	- Input:
```cpp
istream& operator>>(istream& is, Entry& e)
     // read { "name", number } pair. Note: formatted with { " ", and }
{
     char c, c2;
     if (is>>c && c=='{' && is>>c2 && c2=='"') { // start with a { "
           string name;                   // the default value of a string is the empty string: ""
           while (is.get(c) && c!='"')    // anything before a " is part of the name
                 name+=c;

           if (is>>c && c==',') {
                 int number = 0;
                 if (is>>number>>c && c=='}') { // read the number and a }
                        e = {name,number};      // assign to the entry
                        return is;
                 }
           }
     }
     is.setstate(ios_base::failbit);      // register the failure in the stream
     return is;
}
```
	- Output:
```cpp
ostream& operator<<(ostream& os, const Entry& e) {
     return os << "{\"" << e.name << "\", " << e.number << "}";
}
```

## 10.7 File Streams
```cpp
#include <fstream>
ofstream ofs {"target"};               // "o" for "output"
if (!ofs)
    error("couldn't open 'target' for writing");

ifstream ifs {"source"};               // "i" for "input"
if (!ifs)
    error("couldn't open 'source' for reading");
```

## 10.8 String Stream
- Split word:
```cpp
```cpp
#include<iostream>  
#include<sstream>
#include<string>  
using namespace std;  
int main(){  
    string str="i am a boy";  
    istringstream is(str);  
    string s;  
    while(is>>s)  {  
        cout<<s<<endl;  
    }  
}
```
- Input and output:
```cpp
#include <sstream>

void test() {
     ostringstream oss;

     oss << "{temperature," << scientific << 123.4567890 << "}";
}

template<typename Target =string, typename Source =string>
Target to(Source arg) {
  stringstream interpreter;
  Target result;

  if (!(interpreter << arg)                 // write arg into stream
      || !(interpreter >> result)           // read result from stream
      || !(interpreter >> std::ws).eof())   // stuff left in stream?
      throw runtime_error{"to<>() failed"};

  return result;
}
```

## 10.10 File System
```cpp
#include <filesystem>
```