// boj 10250 ACM 호텔
// bronze 2

#include<iostream>
#include<vector>

using namespace std;

int main(int argc, char *argv[])
{
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;

    int h, w, n;


    for (int i = 0; i < t; i++)
    {
        cin >> h >> w >> n;
        int height=1, width=1;
        for (int j = 0; j < n; j++)
        {           
            if (height > h)
            {
                height = 1;
                width++;
            }
            height++;
        }    
        cout << (height-1) * 100 + width << '\n';
    }
    
    return 0;
}
