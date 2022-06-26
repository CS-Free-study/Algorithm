// boj 2475 검증수
// bronze 5

#include<iostream>

using namespace std;

int main()
{
	int a, b = 0;
	for (int i = 0; i < 5; i++)
	{
		cin >> a;
		b += a * a;
	}
	cout << b % 10;
	return 0;
}