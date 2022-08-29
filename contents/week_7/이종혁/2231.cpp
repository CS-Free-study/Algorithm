// boj 2231 분해합
// bronze 2
#include<iostream>


using namespace std;

int main(int argc, char *argv[])
{ 
    ios_base::sync_with_stdio(false);

    int n;
    cin >> n;
    int sum, part;

    for (int i = 1; i < n; i++)
    {
        sum = i;
        part = i;
        while (part)
        {
            sum += part%10;
            part /= 10;
        }
        if (n == sum)
        {
            cout << i;
            return 0;
        }
    }
    cout << 0;

    return 0;
}