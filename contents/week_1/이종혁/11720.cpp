// boj 11720 숫자의 합
// bronze 4

#include<iostream>
#include<cstring>

using namespace std;

int main(int argc, char * argv[])
{
	int n, sum = 0;
	string a;
	cin >> n >> a;
	for (int i = 0; i < a.length(); i++)
		sum +=(int)a[i]-(int)'0';
	cout << sum;
	return 0;
}