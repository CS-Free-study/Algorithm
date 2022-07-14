// boj 8958 OX 퀴즈
// brozne 2

#include<iostream>
#include<string>


using namespace std;

int main(int argc, char* argv[])
{
	ios_base::sync_with_stdio(false);
	
	string exam;
	int n, result, weight;

	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> exam;
		result = 0;
		weight = 1;
		for (int j = 0; j < exam.length(); j++)
		{
			if (exam[j] == 'O')
				result += (weight++);
			else
				weight = 1;
		}
		cout << result << '\n';
	}

	
	return 0;
}