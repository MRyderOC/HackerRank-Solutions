#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'acmTeam' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts STRING_ARRAY topic as parameter.
 */

    // topic_known, teams = 0, 0
    // for p1, p2 in combinations(topic, 2):
    //     tmp_topic_known = 0
    //     for ch1, ch2 in zip(p1, p2):
    //         if ch1 == "1" or ch2 == "1":
    //             tmp_topic_known += 1
    //     if tmp_topic_known > topic_known:
    //         topic_known = tmp_topic_known
    //         teams = 1
    //     elif tmp_topic_known == topic_known:
    //         teams += 1

    // return [topic_known, teams]


int topicsKnown(string p1, string p2) {
    int topics_known = 0;
    for (int i = 0; i < p1.size(); i++)
        if (p1[i] == '1' || p2[i] == '1')
            topics_known++;

    return topics_known;
}


vector<int> acmTeam(vector<string> topic) {
    int topics_known = 0, teams = 0;
    for (int i = 0; i < topic.size() - 1; i++)
        for (int j = i + 1; j < topic.size(); j++) {
            int tmp_topic_known = topicsKnown(topic[i], topic[j]);
            if (tmp_topic_known > topics_known) {
                topics_known = tmp_topic_known;
                teams = 1;
            } else if (tmp_topic_known == topics_known) {
                teams++;
            }
        }

    return vector<int> {topics_known, teams};
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string first_multiple_input_temp;
    getline(cin, first_multiple_input_temp);

    vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

    int n = stoi(first_multiple_input[0]);

    int m = stoi(first_multiple_input[1]);

    vector<string> topic(n);

    for (int i = 0; i < n; i++) {
        string topic_item;
        getline(cin, topic_item);

        topic[i] = topic_item;
    }

    vector<int> result = acmTeam(topic);

    for (size_t i = 0; i < result.size(); i++) {
        fout << result[i];

        if (i != result.size() - 1) {
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
