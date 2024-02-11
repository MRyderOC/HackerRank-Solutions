#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'beautifulTriplets' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER d
 *  2. INTEGER_ARRAY arr
 */

    // triplets_count = 0
    // count_map = defaultdict(int)
    // for item in arr:
    //     count_map[item] += 1

    // for k, v in count_map.items():
    //     k_plus_d = count_map.get(k + d, 0)
    //     k_plus_2d = count_map.get(k + (2 * d), 0)
    //     triplets_count += (v * k_plus_d * k_plus_2d)

    // return triplets_count

int beautifulTriplets(int d, vector<int> arr) {
    int triplets_count = 0;
    map<int, int> count_map;
    for (auto elem: arr) {
        if (count_map.find(elem) != count_map.end())
            count_map[elem]++;
        else
            count_map[elem] = 1;
    }
    for (auto elem: count_map) {
        int k_plus_d = 0, k_plus_2d = 0;
        if (auto search_d = count_map.find(elem.first + d); search_d != count_map.end())
            k_plus_d = search_d->second;
        if (auto search_2d = count_map.find(elem.first + (2 * d)); search_2d != count_map.end())
            k_plus_2d = search_2d->second;

        triplets_count += (elem.second * k_plus_d * k_plus_2d);
    }

    return triplets_count;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string first_multiple_input_temp;
    getline(cin, first_multiple_input_temp);

    vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

    int n = stoi(first_multiple_input[0]);

    int d = stoi(first_multiple_input[1]);

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split(rtrim(arr_temp_temp));

    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    int result = beautifulTriplets(d, arr);

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
