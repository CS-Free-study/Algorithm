// boj 10818 최소, 최대
// bronze 3

#include<iostream>

using namespace std;


int main(int argc, char * argv[])
{
	int min=1000000, max=-1000000, n,a;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> a;
		if (min > a)
			min = a;
		if (max < a)
			max = a;
	}
	cout << min << " " << max ;

	return 0;
}