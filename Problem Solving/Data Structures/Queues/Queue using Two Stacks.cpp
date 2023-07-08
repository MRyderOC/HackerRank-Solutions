#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */

    queue<int> q;

    int number_of_queries;
    cin >> number_of_queries;
    for (int i = 0; i < number_of_queries; i++) {
        int q_type;
        cin >> q_type;
        switch (q_type) {
            case 1: {
                int x;
                cin >> x;
                q.push(x);
                break;
            }

            case 2: {
                q.pop();
                break;
            }

            case 3: {
                cout << q.front() << endl;
                break;
            }
        }
    }

    return 0;
}
