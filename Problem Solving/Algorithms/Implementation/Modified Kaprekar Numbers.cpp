#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'kaprekarNumbers' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER p
 *  2. INTEGER q
 */
// def is_kaprekar(n):
//     if n == 1:
//         return True

//     digits = len(str(n))
//     n_squared = n ** 2
//     first_half_str = str(n_squared)[:-digits]
//     secon_half_str = str(n_squared)[-digits:]
//     first_half = 0 if not first_half_str else int(first_half_str)
//     secon_half = 0 if not first_half_str else int(secon_half_str)
//     if first_half + secon_half == n:
//         return True
//     return False


bool isKaprekar(long n) {
    if (n == 1)
        return true;
    long num_of_digits = 0, new_n = n, n_squared = n * n;
    while (new_n > 0) {
        num_of_digits++;
        new_n /= 10;
    }
    long first_half = n_squared % (long)(pow(10, num_of_digits));
    long second_half = n_squared / (long)(pow(10, num_of_digits));
    // cout << first_half << " - "<< second_half << endl;
    if (first_half + second_half == n)
        return true;
    return false;
}

void kaprekarNumbers(int p, int q) {
    vector<long> out;
    for (long i = p; i <= q; i++)
        if (isKaprekar(i))
            out.push_back(i);

    if (out.empty())
        cout << "INVALID RANGE";
    else
        for (long j: out)
            cout << j << " ";

}

int main()
{
    string p_temp;
    getline(cin, p_temp);

    int p = stoi(ltrim(rtrim(p_temp)));

    string q_temp;
    getline(cin, q_temp);

    int q = stoi(ltrim(rtrim(q_temp)));

    kaprekarNumbers(p, q);

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
