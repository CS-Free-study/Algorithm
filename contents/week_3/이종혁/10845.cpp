// boj 10845 
// silver 4

#include<iostream>
#include<string>
#include<queue>

using namespace std;


int main(int argc, char * argv[])
{
	ios_base::sync_with_stdio(false);
	
	int n, front;                 // 반복횟수, front 포인터
	cin >> n;
	string command;           // 입력받을 명령어
	queue<int> queue;

	for (int i = 0; i < n; i++)
	{
		cin >> command;
		if(command == "push")
		{
			int data;
			cin >> data;
			queue.push(data);
		}
		else if(command == "pop")
		{
			if (queue.size() != 0)
			{
				front = queue.front();
				queue.pop();
			}
			else
				front = -1;
			cout << front << '\n';
		}
		else if(command == "front")
		{
			if (queue.size() == 0)
				front = -1;
			else
				front = queue.front();
			cout << front << '\n';
		}
		else if (command == "back")
		{
			if (queue.size() == 0)
				front = -1;
			else
				front = queue.back();
			cout << front << '\n';
		}
		else if (command == "size")
		{
			cout << queue.size() << '\n';
		}
		else if (command == "empty")
		{
			if (queue.size() == 0)
				front = 1;
			else
				front = 0;
			cout << front << '\n';
			
		}
	}

	
	return 0;
}