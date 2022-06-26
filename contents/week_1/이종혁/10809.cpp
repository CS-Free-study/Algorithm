// boj 10809 알파벳 찾기 
// bronze 5

#include<iostream>
#include<cstring>

using namespace std;

int main()
{
	bool check;
	string word;
	cin >> word;
	for (char i = 'a'; i <= 'z'; i++)
	{
		check = false;
		for (int j = 0; j < word.length(); j++)
		{
			if (word[j] == i)
			{
				check = true;
				cout << j << " ";
				break;
			}
		}
		if (!check)
			cout << "-1 ";
	}
	return 0;
}