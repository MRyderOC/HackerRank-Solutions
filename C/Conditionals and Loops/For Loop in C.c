#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void print_odd_or_even(int a){
    if (a % 2 == 0) printf("even");
    else printf("odd");
}
void print_1_to_9(int a){
    if (a == 1) printf("one");
    else if (a==2) printf("two");
    else if (a==3) printf("three");
    else if (a==4) printf("four");
    else if (a==5) printf("five");
    else if (a==6) printf("six");
    else if (a==7) printf("seven");
    else if (a==8) printf("eight");
    else if (a==9) printf("nine");
    else printf("Greater than 9");
}

int main() 
{
    int a, b;
    scanf("%d\n%d", &a, &b);
  	// Complete the code.
    for (int i = a; i <= b; i++){
        if (i <= 9)
            print_1_to_9(i);
        else
            print_odd_or_even(i);
        printf("\n");
        
    }

    return 0;
}

