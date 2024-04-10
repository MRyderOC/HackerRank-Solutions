#include <bits/stdc++.h>

using namespace std;



int main()
{
    string S;
    getline(cin, S);
    int i;
    try {
        i = stoi(S);
        cout << i;
    } catch (invalid_argument) {
        cout << "Bad String";
    }

    return 0;
}
