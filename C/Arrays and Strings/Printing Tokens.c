#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    char *s;
    s = malloc(1024 * sizeof(char));
    scanf("%[^\n]", s);
    s = realloc(s, strlen(s) + 1);
    //Write your logic to print the tokens of the sentence here.
    char tmp;
    while(1) {
        if(*s == ' ') printf("\n");
        else if(*s == '\0') break;
        else printf("%c", *s);
        s++;
    }
    return 0;
}