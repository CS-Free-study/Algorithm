// boj 2292 벌집
// bronze 2

#include<iostream>

using namespace std;

int main(int argc, char *argv[])
{
    ios_base::sync_with_stdio(false);

    int n, sum=1;
    cin >> n;
    
    for (int i = 1; i <= n; i++)
    {
        if (n <= sum)
        {
            cout << i;
            return 0;
        }        
        sum += i * 6;
    }

    return 0;
}