# Stream

## String stream
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