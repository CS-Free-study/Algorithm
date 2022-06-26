// boj 10952 A+B-5
// bronze 5

#include<iostream>

using namespace std;

int main(int argc, char * argv[])
{
	int a, b;
	while (true)
	{
		cin >> a >> b;
		if (a==0 && b==0)
			break;
		cout << a + b << '\n';
	}
	
	return 0;
}