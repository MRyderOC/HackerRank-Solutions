#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'getMax' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts STRING_ARRAY operations as parameter.
 */

vector<int> getMax(vector<string> operations) {
    vector<int> stack;
    vector<int> out;
    vector<int> max_vec;
    for (auto s: operations) {
        switch (s[0]) {
            case '1': {
                int x = stoi(s.substr(2));
                stack.push_back(x);
                if (max_vec.empty())
                    max_vec.push_back(x);
                else if (max_vec.back() <= x)
                    max_vec.push_back(x);
                else
                    max_vec.push_back(max_vec.back());
                break;
            }
            case '2':
                stack.pop_back();
                max_vec.pop_back();
                break;

            case '3':
                out.push_back(max_vec.back());
                break;
        }
    }

    return out;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    vector<string> ops(n);

    for (int i = 0; i < n; i++) {
        string ops_item;
        getline(cin, ops_item);

        ops[i] = ops_item;
    }

    vector<int> res = getMax(ops);

    for (size_t i = 0; i < res.size(); i++) {
        fout << res[i];

        if (i != res.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

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
