#include <iostream>
#include <cstdio>
using namespace std;

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max_of_two(int a, int b) {
    return a > b ? a : b;
}

int max_of_four(int a, int b, int c, int d) {
    int max1 = max_of_two(a, b);
    int max2 = max_of_two(c, d);
    return max_of_two(max1, max2);
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}
