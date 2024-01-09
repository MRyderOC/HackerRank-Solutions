#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'hackerrankInString' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

    // h_idx = 0
    // h_str = "hackerrank"
    // s_idx = 0
    // while s_idx < len(s) and h_idx < len(h_str):
    //     if s[s_idx] == h_str[h_idx]:
    //         h_idx += 1
    //     s_idx += 1

    // if h_idx == len(h_str):
    //     return "YES"
    // return "NO"


string hackerrankInString(string s) {
    int h_idx = 0, s_idx = 0;
    string h_str = "hackerrank";
    while (s_idx < s.size() && h_idx < h_str.size()) {
        if (s[s_idx] == h_str[h_idx])
            h_idx++;
        s_idx++;
    }

    if (h_idx == h_str.size())
        return "YES";
    return "NO";
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

        string result = hackerrankInString(s);

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
