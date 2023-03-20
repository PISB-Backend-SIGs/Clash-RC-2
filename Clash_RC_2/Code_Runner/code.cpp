#include <iostream>
#include <st
using namespace std;

string reverse_string(string s) {
    string reversed = "";
    for (int i = s.length() - 1; i >=0; i--) {
        reversed += s[i];
    }
    return reversed;
}

int main() {
    string s;
    cin>>s;
    string reversed_s = reverse_string(s);
    cout << reversed_s << endl;
    return 0;
}