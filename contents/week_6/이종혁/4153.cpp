// boj 4153 직각삼각형
// bronze 3

#include<iostream>

using namespace std;

int main(int argc, char argv[])
{
    int a, b, c;
    while (true)
    {
        cin >> a >> b >> c;
        if (a == 0 && b == 0 && c == 0)
            break;

        if (a > b)
        {
            if (a > c)
            {
                if (a * a == b * b + c * c)
                    cout << "right" << '\n';
                else
                    cout << "wrong" << '\n';
            }
            else
            {
                if (c * c == a * a + b * b)
                    cout << "right" << '\n';
                else
                    cout << "wrong" << '\n';
            }
        }
        else
        {
            if (b > c)
            {
                if (b * b == a * a + c * c)
                    cout << "right" << '\n';
                else
                    cout << "wrong" << '\n';
            }
            else
            {
                if (c * c == a * a + b * b)
                    cout << "right" << '\n';
                else
                    cout << "wrong" << '\n';
            }
        }
    }
    
    
    return 0;
}