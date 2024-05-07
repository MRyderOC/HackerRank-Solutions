#include <bits/stdc++.h>
#include <map>

using namespace std;

/*
 * Complete the 'gameOfThrones' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

string gameOfThrones(string s) {
    map<char, int> freq;
    for (char ch: s) {
        if (freq.find(ch) == freq.end())
            freq[ch] = 1;
        else
            freq[ch]++;
    }

    int odds = 0;
    for (auto p: freq)
        if (p.second % 2 == 1)
            odds++;

    if (s.size() % 2 == 1) {
        if (odds <= 1)
            return "YES";
        return "NO";
    } else {
        if (odds > 0)
            return "NO";
        return "YES";
    }

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = gameOfThrones(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
