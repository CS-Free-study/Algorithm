// boj 2577 숫자의 개수
// bronze 2

#include<iostream>
#include<string>


using namespace std;


int main(int argc, char * argv[])
{
	ios_base::sync_with_stdio(false);
	
	int num[10] = {0};
	int a, b, c;
	cin >> a >> b >> c;
	string n = to_string(a * b * c);
	for (int i = 0; i < n.length(); i++)
	{
		for (int j = 0; j < 10; j++)
		{
			if (n[i] == (char)(j+48))
				num[j]++;
		}
	}
	for (int i = 0; i < 10; i++)
		cout << num[i] << '\n';
	return 0;
}