#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'separateNumbers' function below.
 *
 * The function accepts STRING s as parameter.
 */

void separateNumbers(string s) {
    if (s.size() == 0 || s[0] == '0') {
        cout << "NO" << endl;
        return;
    }

    bool flag = false;
    int k = 1;
    long n;
    while (k <= (s.size() / 2) + 1) {
        n = std::atol(s.substr(0, k).c_str());
        string tmp = to_string(n);
        int i = 1;
        while (tmp.size() < s.size()) {
            tmp = tmp + to_string(n + i);
            i++;
            
            if (tmp == s) {
                flag = true;
                break;
            }
        }
        if (flag)
            break;
        k++;
    }

    if (flag)
        cout << "YES " << n << endl;
    else
        cout << "NO" << endl;
}

int main()
{
    string q_temp;
    getline(cin, q_temp);

    int q = stoi(ltrim(rtrim(q_temp)));

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string s;
        getline(cin, s);

        separateNumbers(s);
    }

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
