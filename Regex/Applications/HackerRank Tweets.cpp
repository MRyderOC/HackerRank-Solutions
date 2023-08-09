#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <regex>

using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    regex regex_pattern ("hackerrank", regex::icase);
    int count = 0;
    int n;
    cin >> n;
    for (int i = 0; i <= n; i++) {
        string s;
        getline(cin, s);
        if (regex_search(s, regex_pattern))
            count++;
    }
    cout << count;

    return 0;
}
