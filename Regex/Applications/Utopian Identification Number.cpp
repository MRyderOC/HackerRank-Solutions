#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <regex>

using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    regex regex_pattern {"^[a-z]{0,3}\\d{2,8}[A-Z]{3,}$"};
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string row_input;
        cin >> row_input;
        if (regex_search(row_input, regex_pattern))
            cout << "VALID" << endl;
        else
            cout << "INVALID" << endl;
    }

    return 0;
}
