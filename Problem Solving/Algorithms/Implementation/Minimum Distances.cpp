#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'minimumDistances' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY a as parameter.
 */


int minimumDistances(vector<int> a) {
    map<int, vector<int>> item_idx_map;
    for (int i = 0; i < a.size(); i++) {
        if (item_idx_map.find(a[i]) == item_idx_map.end())
            item_idx_map[a[i]] = vector<int> {i};
        else
            item_idx_map[a[i]].push_back(i);
    }

    vector<int> min_dist;
    for (auto p: item_idx_map) {
        auto item_idx_vec = p.second;
        if (item_idx_vec.size() == 1)
            continue;

        vector<int> tmp_vec;
        for (int i = 0; i < item_idx_vec.size() - 1; i++)
            tmp_vec.push_back(item_idx_vec[i + 1] - item_idx_vec[i]);

        min_dist.push_back(*min_element(tmp_vec.begin(), tmp_vec.end()));
    }

    if (min_dist.size() > 0)
        return *min_element(min_dist.begin(), min_dist.end());
    return -1;
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

    int result = minimumDistances(a);

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
