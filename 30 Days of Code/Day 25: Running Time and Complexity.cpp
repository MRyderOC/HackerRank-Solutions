#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void isPrime(int n) {
    bool primeFlag = true;
    if (n == 1)
        primeFlag = false;
    else if (n == 2)
        primeFlag = true;
    else {
        for (int i = 2; i <= (int)ceil(sqrt(n)); i++)
            if (n % i == 0)
                primeFlag = false;
    }

    if (primeFlag)
        cout << "Prime" << endl;
    else
        cout << "Not prime" << endl;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        isPrime(n);
    }

    return 0;
}
