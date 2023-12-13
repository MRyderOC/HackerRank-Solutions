#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'pickingNumbers' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY a as parameter.
 */

    // max_length = 0
    // counter = Counter(a)
    // for k, v in counter.items():
    //     max_length = max(
    //         max_length,
    //         v + counter.get(k - 1, 0),
    //         v + counter.get(k + 1, 0))

    // return max_length


int pickingNumbers(vector<int> a) {
    int max_length = 0;
    map<int, int> the_counter;
    for (int i = 0; i < a.size(); i++)
        if (the_counter.find(a[i]) == the_counter.end())
            the_counter[a[i]] = 1;
        else
            the_counter[a[i]]++;

    for (auto p: the_counter) {
        int plus_one_len = the_counter[p.first], minus_one_len = the_counter[p.first];
        if (the_counter.find(p.first - 1) != the_counter.end())
            minus_one_len = the_counter[p.first] + the_counter[p.first - 1];
        if (the_counter.find(p.first + 1) != the_counter.end())
            plus_one_len = the_counter[p.first] + the_counter[p.first + 1];
        int new_len_max = max(minus_one_len, plus_one_len);
        max_length = max(new_len_max, max_length);
    }

    return max_length;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    string a_temp_temp;
    getline(cin, a_temp_temp);

    vector<string> a_temp = split(rtrim(a_temp_temp));

    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        int a_item = stoi(a_temp[i]);

        a[i] = a_item;
    }

    int result = pickingNumbers(a);

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

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
