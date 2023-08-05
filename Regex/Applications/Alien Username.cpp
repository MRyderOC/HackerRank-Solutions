#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <regex>

using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    regex username_pattern {"^[_|.]\\d+[a-zA-Z]*_?$"};

    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string row_input;
        cin >> row_input;
        if (regex_search(row_input, username_pattern))
            cout << "VALID" << endl;
        else
            cout << "INVALID" << endl;
    }
    
    return 0;
}
