#include <iostream>
#include <cstdio>
#include <iomanip>
using namespace std;

int main() {
    // Complete the code.
    int a;
    long b;
    char c;
    float d;
    double e;
    cin >> a >> b >> c >> d >> e;
    cout << a << endl << b << endl << c << endl << setprecision(10) << d << endl << setprecision(20) << e;
    // printf("%d\n%ld\n%c\n%f\n%lf", a, b, c, d, e);

    return 0;
}