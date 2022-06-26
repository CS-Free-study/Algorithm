// boj 2439 별 찍기 -2 
// bronze 4

#include<iostream>

using namespace std;

int main(int argc, char * argv[])
{
	int a;
	cin >> a;
	for (int i = 1; i <=a; i++)
	{
		for (int j = a; j-i> 0; j--)
			cout << " ";

		for (int k = 1; k <=i; k++)
			cout << "*";
		cout << '\n';
	}
	
	return 0;
}