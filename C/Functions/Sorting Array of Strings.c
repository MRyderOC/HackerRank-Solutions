#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int number_of_distinct_characters(const char* a) {
    int distinct_arr[26] = {0};
    const char *ptr = a;
    while (*ptr) {
        int char_int = *ptr - 97;
        distinct_arr[char_int]++;
        ptr++;
    }

    int count_distinct = 0;
    for (int i = 0; i < 26; i++)
        if (distinct_arr[i] > 0)
            count_distinct++;

    return count_distinct;
}

int lexicographic_sort(const char* a, const char* b) {
    return strcmp(a, b);
}

int lexicographic_sort_reverse(const char* a, const char* b) {
    return -strcmp(a, b);
}

int sort_by_number_of_distinct_characters(const char* a, const char* b) {
    int distinct_char_dif = number_of_distinct_characters(a) - number_of_distinct_characters(b);
    if (distinct_char_dif == 0)
        return lexicographic_sort(a, b);
    else
        return distinct_char_dif;
}

int sort_by_length(const char* a, const char* b) {
    int len_dif = strlen(a) - strlen(b);
    if (len_dif == 0)
        return lexicographic_sort(a, b);
    else
        return len_dif;
}

void string_sort(char** arr,const int len,int (*cmp_func)(const char* a, const char* b)){
    for (int i = 0; i < len - 1; i++)
        for (int j = i + 1; j < len; j++)
            if (cmp_func(arr[i], arr[j]) > 0) {
                // Swap
                char *tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
}


int main() 
{
    int n;
    scanf("%d", &n);

    char** arr;
	arr = (char**)malloc(n * sizeof(char*));

    for(int i = 0; i < n; i++){
        *(arr + i) = malloc(1024 * sizeof(char));
        scanf("%s", *(arr + i));
        *(arr + i) = realloc(*(arr + i), strlen(*(arr + i)) + 1);
    }

    string_sort(arr, n, lexicographic_sort);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");

    string_sort(arr, n, lexicographic_sort_reverse);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");

    string_sort(arr, n, sort_by_length);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);    
    printf("\n");

    string_sort(arr, n, sort_by_number_of_distinct_characters);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");
}