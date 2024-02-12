#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'minimumNumber' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. STRING password
 */

int minimumNumber(int n, string password) {
    // Return the minimum number of characters to make the password strong
    string numbers = "0123456789";
    string lower_case = "abcdefghijklmnopqrstuvwxyz";
    string upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string special_characters = "!@#$%^&*()-+";

    bool has_numbers = false, has_lower_case = false;
    bool has_upper_case = false, has_special_characters = false;
    
    for (auto ch: password) {
        if (numbers.find(ch) != numbers.npos)
            has_numbers = true;
        else if (lower_case.find(ch) != lower_case.npos)
            has_lower_case = true;
        else if (upper_case.find(ch) != upper_case.npos)
            has_upper_case = true;
        else if (special_characters.find(ch) != special_characters.npos)
            has_special_characters = true;
    }

    int count = 0;
    if (has_numbers == false) count++;
    if (has_lower_case == false) count++;
    if (has_upper_case == false) count++;
    if (has_special_characters == false) count++;

    if (password.size() + count < 6)
        return 6 - password.size();
    return count;



}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    string password;
    getline(cin, password);

    int answer = minimumNumber(n, password);

    fout << answer << "\n";

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
