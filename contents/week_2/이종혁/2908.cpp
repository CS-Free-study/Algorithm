// boj 2908 상수
// bronze 2

// 문자열을 거꾸로 뒤집는 reverse(s.begin(), s.end()) 함수
// atoi는 char * 형식이기 때문에 문자열을 char * 형식으로 바꿔주는 s.c_str() 함수
// const char * 를 리턴한다
#include<iostream>
#include<string>
#include<algorithm>

using namespace std;


int main(int argc, char * argv[])
{
	ios_base::sync_with_stdio(false);
	
	string a, b;
	cin >> a >> b;
	reverse(a.begin(), a.end());
	reverse(b.begin(), b.end());
	int num1 = atoi(a.c_str()), num2 = atoi(b.c_str());
	if (num1 > num2)
		cout << num1;
	else
		cout << num2;
	return 0;
}