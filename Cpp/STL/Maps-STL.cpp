#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int q;
    cin >> q;
    map <string, int> m;
    for (int i = 0; i < q; i++) {
        int type;
        cin >> type;
        string X;
        cin >> X;
        switch (type) {
            case 1:
                int Y;
                cin >> Y;
                if (m.find(X) != m.end()) {
                    m[X] += Y;
                } else 
                    m.insert(make_pair(X, Y));
                break;
            case 2:
                m.erase(X);
                break;
            case 3:
                int marks = m[X];
                cout << marks << endl;
                break;
        }
    }

    return 0;
}