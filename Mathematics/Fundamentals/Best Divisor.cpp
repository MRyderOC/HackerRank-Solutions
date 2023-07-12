#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);


bool is_divisor(int n, int i) {
    if (n % i == 0)
        return true;
    return false;
}

int sum_of_digits(int n) {
    int s = 0;
    while (n > 0) {
        s += n % 10;
        n /= 10;
    }
    return s;
}


int main()
{
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    int best_divisor = 0;
    for (int i = 1; i <= n; i++) {
        if (is_divisor(n, i)) {
            if (sum_of_digits(best_divisor) < sum_of_digits(i))
                best_divisor = i;
            if (sum_of_digits(best_divisor) == sum_of_digits(i) && i < best_divisor)
                best_divisor = i;
        }
    }

    cout << best_divisor;

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
