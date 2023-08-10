#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <regex>

using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    regex regex_pattern {"^[A-Z]{5}\\d{4}[A-Z]$"};
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        if (regex_search(s, regex_pattern))
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}
