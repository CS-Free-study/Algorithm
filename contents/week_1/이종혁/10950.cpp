// boj 10950 A+B-3
// bronze 5


#include<iostream>

using namespace std;

int main(int argc, char * argv[])
{
	int n;
	cin >> n;
	int* arr = new int[n];
	for (int i = 0; i < n; i++)
	{
		int a, b;
		cin >> a >> b;
		arr[i] = a + b;		
	}
	for(int i=0; i<n; i++)
		cout << arr[i] << '\n';
	delete[] arr;
	return 0;
}
