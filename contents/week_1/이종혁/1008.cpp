// boj 1008 A/B
// bronze 5

// c++의 소수점 출력은 cout.precision(n) 함수를 사용해야 한다
// n은 정수부+실수부의 합친 자리수
// n을 소수점 아래 자리수로 고정시키고 싶을 떈 cout<<fixed 사용
// cout<<fixed를 해제하고 싶을 떈 cout.unsef(ios::fixed) 사용

#include<iostream>

using namespace std;

int main()
{
	int a = 0, b = 0;
	cin >> a>> b;
	double c = (double)a/b;
	cout.precision(9);
    cout<<fixed;
	cout << c;
    return 0;
}