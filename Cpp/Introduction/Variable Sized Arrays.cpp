#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, q;
    cin >> n >> q;
    vector< vector<int> > vec;

    for (int i = 0; i < n; i++) {
        int k;
        cin >> k;
        vector<int> tmp_vec;
        for (int j = 0; j < k; j++) {
            int tmp_int;
            cin >> tmp_int;
            tmp_vec.push_back(tmp_int);
        }
        vec.push_back(tmp_vec);
    }

    for (int x = 0; x < q; x++) {
        int i, j;
        cin >> i >> j;
        cout << vec[i][j] << endl;
    }

    return 0;
}
