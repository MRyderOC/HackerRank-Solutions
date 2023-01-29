#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;

double area(triangle tr){
    double p = (tr.a + tr.b + tr.c) / 2.0;
    double s = sqrt(p * (p - tr.a) * (p - tr.b) * (p - tr.c));
    return s;
}

int compare_area(const void* a, const void* b)
{
    triangle arg1 = *(const triangle*)a;
    triangle arg2 = *(const triangle*)b;

    if (area(arg1) < area(arg2)) return -1;
    if (area(arg1) > area(arg2)) return 1;
    return 0;
}


void sort_by_area(triangle* tr, int n) {
	/**
	* Sort an array a of the length n
	*/
    qsort(tr, n, sizeof(triangle), compare_area);
}

int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}