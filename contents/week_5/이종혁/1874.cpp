// boj 1874 스택 수열
// sliver 3

#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);

    stack<int> s;
    vector<char> v;

    int n, count = 1;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        while (count <= num)
        {
            s.push(count++);
            v.push_back('+');
        }
        if (s.top() == num)
        {
            s.pop();
            v.push_back('-');
        }
        else
        {
            cout << "NO";
            return 0;
        }
    }
    
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << '\n';
    }

    return 0;
}