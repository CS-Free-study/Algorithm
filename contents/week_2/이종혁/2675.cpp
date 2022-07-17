// boj 2675 문자열 반복
// bronze 2

#include<iostream>
#include<string>


using namespace std;


int main(int argc, char * argv[])
{
	ios_base::sync_with_stdio(false);
	
	int n, r;
	string s;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> r >> s;
		for (int j = 0; j < s.length(); j++)
		{
			for (int k = 0; k < r; k++)
			{
				cout << s[j];
			}
		}
		cout << '\n';
	}

	return 0;
}