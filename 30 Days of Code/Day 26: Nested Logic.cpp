#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int fine;
    int r_d, r_m, r_y;
    int e_d, e_m, e_y;
    cin  >> r_d >> r_m >> r_y;
    cin >> e_d >> e_m >> e_y;

    if (r_y < e_y)
        fine = 0;
    else if (r_y > e_y)
        fine = 10000;
    else {
        if (r_m < e_m)
            fine = 0;
        else if (r_m > e_m)
            fine = 500 * (r_m - e_m);
        else {
            if (r_d <= e_d)
                fine = 0;
            else
                fine = 15 * (r_d - e_d);
        }
    }
    cout << fine;

    return 0;
}
