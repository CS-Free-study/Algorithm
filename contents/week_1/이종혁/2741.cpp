// boj 2741 N 찍기
// bronze 5
// c++ 에서 endl은 단순 개행만 하는 것이 아니라 버퍼를 비우는 작업을 하기 때문에 
// \n 을 사용하여 개행하는 알고리즘 풀이에서는 좋다
// endl을 쓸 경우 시간초과 발생

// 방법 1
#include<iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		cout << i << '\n';
	}
	return 0;
}



// 방법 2
// c++과 c의 표준 스트림은 동기화가 되어있기 때문에 이를 
// ios_base::sync_with_stdio(false) 코드를 통해 동기화를 끊어주면
// c++ 스트림들은 독립적인 버퍼를 갖게되고 버퍼의 수가 줄어들어 입출력 속도가 빨라진다
// 실제로 위의 두개의 코드는 속도가 2배 차이났다.
// 하지만, 위 코드 사용시 c의 표준 입출력(scanf, printf, getchar)등의 함수는 사용할 수 없다.
// cin.tie(NULL), cout.tie(NULL)은 입출력 연결을 끊어 입출력시 버퍼를 비우는 역할을 한다
// 입출력을 번갈아가면서 사용할 떄 속도 향상에 유용하다


// #include<iostream>

// using namespace std;

// int main()
// {
// 	ios_base::sync_with_stdio(false);

// 	int n;
// 	cin >> n;
// 	for (int i = 1; i <= n; i++)
// 	{
// 		cout << i << '\n';
// 	}
// 	return 0;
// }