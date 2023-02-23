#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    vector<int> vec;
    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        vec.push_back(tmp);
    }

    int q;
    cin >> q;
    for (int i = 0; i < q; i++) {
        int y;
        cin >> y;
        vector<int>::iterator lb = lower_bound(vec.begin(), vec.end(), y);
        // Alternative: auto lb = lower_bound(vec.begin(), vec.end(), y);
        int lb_idx = lb - vec.begin() + 1;
        // Alternative: auto lb_idx = lb - vec.begin() + 1;
        if (y == *lb)
            cout << "Yes " << lb_idx << endl;
        else
            cout << "No " << lb_idx << endl;
    }

    return 0;
}
