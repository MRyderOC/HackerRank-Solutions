#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    string s;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> s;
        for (int e_idx = 0; e_idx < s.size(); e_idx += 2)
            cout << s[e_idx];
        cout << " ";
        for (int o_idx = 1; o_idx < s.size(); o_idx += 2)
            cout << s[o_idx];
        cout << endl;
    }
    return 0;
}
