#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int max(int a, int b) {
    return a > b? a : b;
}

int main() 
{
    int n;
    scanf("%d", &n);

  	// Complete the code to print the pattern.
    for(int i = 0; i < 2 * n - 1; i++) {
        for(int j = 0; j < 2 * n - 1; j++) {
            int to_print = max(abs(n - i - 1) + 1, abs(n - j - 1) + 1);
            printf("%d ", to_print);
        }
        printf("\n");
    }

    return 0;
}
