// boj 2562 최댓값
// bronze 3

#include<iostream>
#include<cstring>

using namespace std;

int main(int argc, char * argv[])
{
	int arr[9];
	int index=1, max;
	for (int i = 0; i < 9; i++)
		cin >> arr[i];
	max = arr[0];
	for (int i = 1; i < 9; i++)
	{
		if (arr[i] > max)
		{
			max = arr[i];
			index = i+1;
		}		
	}
	cout << max << '\n' << index;
	return 0;
}