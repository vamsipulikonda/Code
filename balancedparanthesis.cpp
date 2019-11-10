#include <iostream>
#include<stack>
#include<string>
using namespace std;

string balanced(string s){
    stack<char> st;
    for(auto c:s){
        switch(c){
        case '{' :
        case '[':
        case '(':
            st.push(c);
            break;
        case '}':
            if(st.empty() || st.top() != '{'){
                return "NO";
            }
            st.pop();
            break;
        case ']':
            if(st.empty() || st.top() != '['){
                return "NO";
            }
            st.pop();
            break;
        case ')':
            if(st.empty() || st.top() != '('){
                return "NO";
            }
            st.pop();
            break;
        }
    }
    return st.empty() ? "YES" : "NO";
}
int main() {
    string s;
    cin >> s;
    cout << balanced(s);
}
