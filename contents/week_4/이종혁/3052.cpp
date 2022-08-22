// boj 3052 나머지
// bronze 2

#include<iostream>
#include<string>


using namespace std;

int main(int argc, char* argv[])
{
	ios_base::sync_with_stdio(false);
	int r[10] ;
	int a, count=0;

	for (int i = 0; i < 10; i++)
	{
		r[i] = -1;
	}


	for (int i = 0; i < 10; i++)
	{
		bool check = true;
		cin >> a;
		a = a % 42;
		
		for (int j = 0; j < 10; j++)
		{
			if (r[j] == a)
				check = false;
		}
		r[i] = a;
		if (check)
			count++;
	}

	cout << count;


	return 0;
}