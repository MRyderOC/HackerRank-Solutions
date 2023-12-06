#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'migratoryBirds' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

bool val_comp_max(const pair<int, int> &a, const pair<int, int> &b) {
   return a.second < b.second;
}

int migratoryBirds(vector<int> arr) {

    // max_sighting = max(d.values())
    // return min([k for k, v in d.items() if v == max_sighting])
    map<int, int> d;
    for (int i = 0; i < arr.size(); i++) {
        if (d.find(arr[i]) != d.end())
            d[arr[i]]++;
        else
            d[arr[i]] = 1;
    }
    int max_sighting = max_element(
        d.begin(), d.end(), val_comp_max)->second;
    int min_val = INT32_MAX;
    for (auto d_pair : d) {
        if (d_pair.second != max_sighting) continue;
        if (d_pair.first < min_val) min_val = d_pair.first;
    }

    return min_val;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string arr_count_temp;
    getline(cin, arr_count_temp);

    int arr_count = stoi(ltrim(rtrim(arr_count_temp)));

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split(rtrim(arr_temp_temp));

    vector<int> arr(arr_count);

    for (int i = 0; i < arr_count; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    int result = migratoryBirds(arr);

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
