// boj 1003 피보나치 함수
// silver 3

#include<stdio.h>

void fibonacci(int n);



int main(void)
{
	int k;
	scanf("%d", &k);
	for (int i = 0; i < k; i++)
	{
		int t;
		scanf("%d", &t);
		fibonacci(t);
		
	}
	

}

void fibonacci(int n)
{
	int a = 0, b = 1, c=0;
	if (n == 0)
	{
		printf("1 0\n");
	}
	else
	{
		for (int i = 1; i < n; i++)
		{
			c = a + b;
			a = b;
			b = c;
		}
		printf("%d %d\n", a, b);
		
	}
}


