// boj 1330 두 수 비교하기
// bronze 5
// cout 에서의 삼항연산자 사용

#include<iostream>

using namespace std;

int main()
{
	int a, b;
	cin >> a >> b;
	cout <<((a > b) ? ">" :(a < b) ? "<" : "==");
	return 0;
}