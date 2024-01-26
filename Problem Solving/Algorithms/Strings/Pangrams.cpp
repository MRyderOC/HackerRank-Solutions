#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'pangrams' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

string pangrams(string s) {
    vector<bool> seen(25, false);
    for (auto ch: s) {
        int ch_idx;
        if (int(ch) >= 65 && int(ch) <= 90)
            ch_idx = int(ch) - 65;
        else if (int(ch) >= 97 && int(ch) <= 122)
            ch_idx = int(ch) - 97;
        else
            continue;

        seen[ch_idx] = true;
    }

    bool is_all_true = all_of(
        seen.begin(), seen.end(),
        [](bool elem){return elem == true;});
    if (is_all_true)
        return "pangram";
    return "not pangram";
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = pangrams(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
