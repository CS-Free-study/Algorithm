// boj 2884 알람 시계
// bronze 3

#include<iostream>
#include<cstring>

using namespace std;

int main(int argc, char * argv[])
{
	int h, m;
	cin >> h>>m;
	if (m >= 45)
		m -= 45;
	else
	{
		m += 15;
		if (h == 0)
			h = 23;
		else
			h -= 1;
	}
	cout << h << " " << m;
	return 0;
}