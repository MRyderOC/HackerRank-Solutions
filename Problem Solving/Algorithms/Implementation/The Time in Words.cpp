#include <bits/stdc++.h>
#include <map>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'timeInWords' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. INTEGER h
 *  2. INTEGER m
 */

string timeInWords(int h, int m) {
    std::map<int, std::string> number_word = {
        {1, "one"},
        {2, "two"},
        {3, "three"},
        {4, "four"},
        {5, "five"},
        {6, "six"},
        {7, "seven"},
        {8, "eight"},
        {9, "nine"},
        {10, "ten"},
        {11, "eleven"},
        {12, "twelve"},
        {13, "thirteen"},
        {14, "fourteen"},
        {15, "quarter"},
        {16, "sixteen"},
        {17, "seventeen"},
        {18, "eighteen"},
        {19, "nineteen"},
        {20, "twenty"},
        {30, "half"}
    };

    std::string hour = number_word[h], mins = number_word[m];
    if (m == 0)
        return hour + " o' clock";
    else if (m == 1)
        return mins + " minute past " + hour;
    else if (m == 15 || m == 30)
        return mins + " past " + hour;
    else if (m < 30) {
        if (m > 20)
            mins = number_word[20] + " " + number_word[m % 10];
        return mins + " minutes past " + hour;
    } else{
        int res = 60 - m;
        hour = number_word[h + 1];
        mins = number_word[res];
        if (res == 1)
            return mins + " minute to " + hour;
        else if (res == 15)
            return mins + " to " + hour;
        else {
            if (res > 20)
                mins = number_word[20] + " " + number_word[m % 10];
            return mins + " minutes to " + hour;
        }
    }

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string h_temp;
    getline(cin, h_temp);

    int h = stoi(ltrim(rtrim(h_temp)));

    string m_temp;
    getline(cin, m_temp);

    int m = stoi(ltrim(rtrim(m_temp)));

    string result = timeInWords(h, m);

    fout << result << "\n";

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
