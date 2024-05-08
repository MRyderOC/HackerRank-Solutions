#include <bits/stdc++.h>
#include <stack>

using namespace std;

/*
 * Complete the 'superReducedString' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

string superReducedString(string s) {
    stack<char> myStack;
    for (auto ch: s) {
        if (myStack.empty())
            myStack.push(ch);
        else if (ch == myStack.top())
            myStack.pop();
        else
            myStack.push(ch);
    }

    if (myStack.empty())
        return "Empty String";

    string outString = "";
    while (!myStack.empty()) {
        outString = myStack.top() + outString;
        myStack.pop();
    }

    return outString;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = superReducedString(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
