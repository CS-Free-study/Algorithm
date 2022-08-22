// boj 10845 큐
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








// ============================================

// c 스타일로 구현

// #include<stdio.h>
// #include<stdlib.h>

// #define MAX_QUEUE_SIZE 5

// typedef struct{
// 	int front;
// 	int rear;
// 	int data[MAX_QUEUE_SIZE];
// }Queue;

// void init_queue(Queue *q)
// {
// 	q->rear = -1;
// 	q->front = -1;
// }

// int is_full(Queue *q)
// {
// 	if(q->rear == MAX_QUEUE_SIZE -1)
// 		return 1;
// 	else
// 		return 0;
// }

// int is_empty(Queue *q)
// {
// 	if(q->front == q-> rear)
// 		return 1;
// 	else
// 		return 0;
// }

// void enqueue(Queue *q, int data)
// {
// 	if(is_full(q))
// 	{
// 		printf("큐가 포화상태");
// 		return ;
// 	}
// 	q->data[++(q->rear)]=data;
// }



// int dequeue(Queue *q)
// {
// 	if(is_empty(q))
// 	{
// 		printf("큐가 공백상태");
// 		return -1;
// 	}
// 	int data=q->data[++(q->front)];
// 	return data;
// }