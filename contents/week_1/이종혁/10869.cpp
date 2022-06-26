// boj 10869 사칙연산
// bronze 5

#include<iostream>
#include<cstring>

using namespace std;

int main()
{
	int a, b;
	cin >> a >> b;
	cout << a + b << "\n" << a - b << "\n" << a * b << "\n" << a / b<<"\n"<<a%b;
	return 0;
}