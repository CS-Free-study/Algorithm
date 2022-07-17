// boj 10808 스택
// silver 4

#include<iostream>
#include<string>

using namespace std;


int main(int argc, char * argv[])
{
	ios_base::sync_with_stdio(false);
	
	int n, p = -1;                 // 반복횟수, 스택 포인터
	cin >> n;
	string command;           // 입력받을 명령어
	int* arr = new int[n];   // 스택으로 사용 할 배열 동적할당

	for (int i = 0; i < n; i++)
	{
		cin >> command;
		if(command == "push")
		{
			int data;
			cin >> data;
			arr[++p] = data;         // 데이터 삽입 후 스택 포인터 +1
		}
		else if(command == "pop")
		{
			if (p>=0)
				cout << arr[p--] << '\n';     // 데이터 출력 후 스택 포인터 -1			
			else
				cout << -1 << '\n';
		}
		else if(command == "top")
		{
			if (p>=0)
				cout << arr[p] << '\n';      // 스택의 top 출력 
			else
				cout << -1 << '\n';
		}
		else if (command == "size")
		{
			cout << p+1 << '\n';          // idx가 스택의 size
		}
		else if (command == "empty")
		{
			if (p>=0)
				cout << 0 << '\n';
			else
				cout << 1 << '\n';
			
		}
	}
	delete[] arr;
	return 0;
}

// =============================================

// Stack 라이브러리 사용

// #include<iostream>
// #include<stack>
// #include<string>

// using namespace std;

// int main(int argc, char * argv[])
// {
//     int n;
//     cin>> n;

//     stack<int> stack;
//     string command;

//     for (int i = 0; i < n; i++)
// 	{
// 		cin >> command;
// 		if(command == "push")
// 		{
// 			int data;
// 			cin >> data;
//             stack.push(data);
// 		}
// 		else if(command == "pop")
// 		{
// 			if(!stack.empty())
//             {
//                 cout<<stack.top()<<'\n';
//                 stack.pop();
//             }
//             else
//                 cout<<-1<<'\n';
// 		}
// 		else if(command == "top")
// 		{
// 			if(!stack.empty())
//                 cout<<stack.top()<<'\n';
//             else
//                 cout << -1 << '\n';
// 		}
// 		else if (command == "size")
// 		{
// 			cout<<stack.size()<<'\n';
// 		}
// 		else if (command == "empty")
// 		{
// 			if(stack.empty())
//                 cout << 1 << '\n';
//             else
//                 cout << 0 << '\n';
// 		}
// 	}
//     return 0;
// }

// ==============================================

// c 스타일로 구현

// #include<stdio.h>

// #define MAX_STACK_SIZE 100

// typedef struct{
// 	int data[MAX_STACK_SIZE];
// 	int top;
// }Stack;

// void init_stack(Stack *st)
// {
// 	st->top=-1;
// }

// int is_empty(Stack * st)
// {
// 	return (st->top==-1);
// }

// int is_full(Stack *st)
// {
// 	return (st->top==(MAX_STACK_SIZE-1));
// }

// void push(Stack *st, int data)
// {
// 	if(is_full(st))
// 	{
// 		fprintf(stderr,"스택 포화 에러\n");
// 		return ;
// 	}
// 	else
// 		st->data[++(st->top)]=data;
// }

// int pop(Stack * st)
// {
// 	if(is_empty(st))
// 	{
// 		fprintf(stderr, "스택 공백 에러\n");
// 		exit(1);
// 	}
// 	else
// 		return st->data[(st->top)--];
// }