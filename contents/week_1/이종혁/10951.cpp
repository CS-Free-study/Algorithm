// boj A+B-4
// bronze 5
// c++ 에서 EOF 처리 방법은 cin.eof()를 사용한다.

#include<iostream>

using namespace std;

int main(int argc, char * argv[])
{
	int a, b;
	while (true)
	{
		cin >> a >> b;
		if (cin.eof())
			break;
		cout << a + b << '\n';
	}
	
	return 0;
}