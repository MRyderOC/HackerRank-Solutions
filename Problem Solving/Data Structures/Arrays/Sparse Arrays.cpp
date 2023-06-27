#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'matchingStrings' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. STRING_ARRAY stringList
 *  2. STRING_ARRAY queries
 */

vector<int> matchingStrings(vector<string> stringList, vector<string> queries) {
    /*
        // Brute-force solution
        vector<int> out;
        for (auto q: queries){
            int count = 0;
            for(auto s: stringList)
                if (s == q)
                    count++;

            out.push_back(count);
        }

        return out;
    */


    // Map Solution
    map<string, int> str_map;
    for (auto s: stringList){
        if(str_map.find(s) == str_map.end()){
            str_map.insert({s, 1});
        } else {
            str_map[s]++;
        }
    }

    vector<int> out;
    for (auto q: queries){
        if(str_map.find(q) == str_map.end()){
            out.push_back(0);
        } else {
            out.push_back(str_map[q]);
        }
    }

    return out;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string stringList_count_temp;
    getline(cin, stringList_count_temp);

    int stringList_count = stoi(ltrim(rtrim(stringList_count_temp)));

    vector<string> stringList(stringList_count);

    for (int i = 0; i < stringList_count; i++) {
        string stringList_item;
        getline(cin, stringList_item);

        stringList[i] = stringList_item;
    }

    string queries_count_temp;
    getline(cin, queries_count_temp);

    int queries_count = stoi(ltrim(rtrim(queries_count_temp)));

    vector<string> queries(queries_count);

    for (int i = 0; i < queries_count; i++) {
        string queries_item;
        getline(cin, queries_item);

        queries[i] = queries_item;
    }

    vector<int> res = matchingStrings(stringList, queries);

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
