#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'funnyString' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

    // ord_dif_s, ord_dif_rev_s = [], []
    // n = len(s)
    // for i in range(n - 1):
    //     ord_dif_s.append(abs(ord(s[i]) - ord(s[i + 1])))
    //     rev_idx = n - i - 1
    //     ord_dif_rev_s.append(abs(ord(s[rev_idx]) - ord(s[rev_idx - 1])))

    // if ord_dif_rev_s == ord_dif_s:
    //     return "Funny"
    // return "Not Funny"
string funnyString(string s) {
    vector<int> ord_dif_s, ord_dif_rev_s;
    int n = s.size(), rev_idx;
    for (int i = 0; i < n - 1; i++) {
        ord_dif_s.push_back(abs(int(s[i] - int(s[i + 1]))));
        rev_idx = n - i - 1;
        ord_dif_rev_s.push_back(abs(int(s[rev_idx]) - int(s[rev_idx - 1])));
    }
    for (int i = 0; i < ord_dif_s.size(); i++)
        if (ord_dif_s[i] != ord_dif_rev_s[i])
            return "Not Funny";
    return "Funny";
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string q_temp;
    getline(cin, q_temp);

    int q = stoi(ltrim(rtrim(q_temp)));

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string s;
        getline(cin, s);

        string result = funnyString(s);

        fout << result << "\n";
    }

    fout.close();

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
