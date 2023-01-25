#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    char num[1000];
    scanf("%s", num);
    int freq_arr[10] = {0};
    int len_num = strlen(num);
    for(int i=0; i < len_num; i++){
        switch (num[i]) {
            case '0': freq_arr[0]++; break;
            case '1': freq_arr[1]++; break;
            case '2': freq_arr[2]++; break;
            case '3': freq_arr[3]++; break;
            case '4': freq_arr[4]++; break;
            case '5': freq_arr[5]++; break;
            case '6': freq_arr[6]++; break;
            case '7': freq_arr[7]++; break;
            case '8': freq_arr[8]++; break;
            case '9': freq_arr[9]++; break;
            default: continue;
        }
    }
    for(int i = 0; i < 10; i++)
        printf("%d ", freq_arr[i]);

    return 0;
}
