// boj 10871 x보다 작은 수
// bronze 5

#include<iostream>

using namespace std;

int main(int argc, char * argv[])
{
	int n, x;
	cin >> n >> x;
	int* arr = new int[n];
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
		if (arr[i] < x)
			cout << arr[i] << " ";
	}
	delete[] arr;
	return 0;
}

