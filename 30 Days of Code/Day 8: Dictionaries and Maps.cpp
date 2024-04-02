#include <cmath>
#include <cstdio>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    map<string, int> m;
    int n;
    cin >> n;

    string s;
    int phoneNumber;

    for(int i = 0; i < n; i++) {
        cin >> s;
        cin >> phoneNumber;

        m[s] = phoneNumber;
    }
    string q;
    while (cin >> q) {
        if(m.find(q) != m.end())
            cout << q << "=" << m[q] << endl;
        else
            cout << "Not found" << endl;
    }

    return 0;
}
