#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <regex>

using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    regex regex_pattern {"^[1-3][0-2][xs0][30Aa][xsu][.,]$"};
    string s;
    getline(cin, s);
    cout << boolalpha << regex_search(s ,regex_pattern);

    return 0;
}
