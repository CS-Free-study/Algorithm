// boj 2798 블랙잭
// bronze 2

#include<iostream>
#include<vector>

using namespace std;

int main(int argc, char *argv[])
{
    ios_base::sync_with_stdio(false);

    int n, blackjack;
    vector<int> v;
    cin >> n >> blackjack;

    int num;
    for (int i = 0; i < n; i++)
    {
        cin >> num;
        v.push_back(num);
    }
    
    int temp, sum = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            for (int k = j + 1; k < n; k++)
            {
                temp = v[i] + v[j] + v[k];
                if (temp > blackjack)
                    continue;
                sum = max(temp, sum);
            }
        }

    }
    cout << sum;
    return 0;
}