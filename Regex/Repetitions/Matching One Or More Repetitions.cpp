#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <regex>

using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    regex regex_pattern {"^\\d+[A-Z]+[a-z]+$"};
    string s;
    getline(cin, s);
    cout << boolalpha << regex_search(s, regex_pattern);

    return 0;
}
