#include <stdio.h>
/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max_2(int a, int b){
    if(a > b)
        return a;
    else
        return b;
}

int max_of_four(int a, int b, int c, int d){
    int max_a_and_b = max_2(a, b);
    int max_c_and_d = max_2(c, d);
    int max_all = max_2(max_a_and_b, max_c_and_d);
    return max_all;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}