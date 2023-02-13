#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int sum(int a, int b, int c) {
    return a + b + c;
}


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int a, b, c;
    cin >> a >> b >> c;
    cout << sum(a, b, c);
    return 0;
}
