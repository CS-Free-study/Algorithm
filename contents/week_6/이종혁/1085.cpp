// boj 1085 직사각형에서 탈출
// bronze 3

#include<iostream>

using namespace std;

int main(int argc, char *argv[])
{
        ios_base::sync_with_stdio(false);

    int x, y, w, h;
    int dis1, dis2;

    cin >> x >> y >> w >> h;

    dis1 = min(x, y);
    dis2 = min(w - x, h - y);
    cout << min(dis1, dis2);

    return 0;
}