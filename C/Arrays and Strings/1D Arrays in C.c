#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int arr_len, sum = 0;
    scanf("%d\n", &arr_len);
    int *arr = malloc(arr_len * sizeof(int));
    for (int i=0; i < arr_len; i++){
        scanf("%d", &arr[i]);
        sum += arr[i];
    }
    free(arr);
    printf("%d", sum);
    return 0;
}