#include <iostream>
#include <cstdio>
using namespace std;


void less_than_9(int a) {
    if (a == 1) cout << "one";
    else if (a == 2) cout << "two";
    else if (a == 3) cout << "three";
    else if (a == 4) cout << "four";
    else if (a == 5) cout << "five";
    else if (a == 6) cout << "six";
    else if (a == 7) cout << "seven";
    else if (a == 8) cout << "eight";
    else if (a == 9) cout << "nine";
    
    cout << endl;
}

void odd_even(int a) {
    if (a % 2 == 0)
        cout << "even";
    else
        cout << "odd";

    cout << endl;
}



int main() {
    // Complete the code.
    int a, b;
    cin >> a >> b;

    for(int i = a; i <= b; i++) {
        if (i <= 9) less_than_9(i);
        else odd_even(i);
    }
    
    return 0;
}